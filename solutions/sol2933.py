import sys
input = sys.stdin.readline


# 2933 미네랄
# 각 칸이 .(빈칸) 또는 x(미네랄)인 r * c 크기의 동굴이 주어지고
# 왼쪽, 오른쪽에서 번갈아가며 높이 n에서 수평방향으로 막대를 던져
# 처음으로 만난 미네랄 한칸을 제거하고 만약 미네랄이 제거되는 것으로 인해
# 공중에 뜨게된 미네랄 덩어리가 있다면 그 미네랄 덩어리는 바닥부분이 바닥
# 또는 다른 미네랄에 닿을 때 까지 수직으로 떨어진다. 단, 동시에 두 개 이상의 미네랄
# 덩어리가 떨어지는 경우는 주어지지 않는다.
def sol2933():
    r, c = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(r)]

    # 미네랄 덩어리를 탐색하고 공중에 떠있다면 낙하시킨다
    def bfs(sr, sc, visited, id):
        # 미네랄 덩어리의 각 열의 바닥부분
        bottoms = [-1] * c

        q = [(sr, sc)]
        visited[sr][sc] = id
        bottoms[sc] = max(bottoms[sc], sr)
        while q:
            nq = []
            for cx, cy in q:
                if cx > 0:
                    nx, ny = cx - 1, cy
                    if board[nx][ny] == 'x' and not visited[nx][ny]:
                        visited[nx][ny] = id
                        bottoms[ny] = max(bottoms[ny], nx)
                        nq.append((nx, ny))
                if cx < r - 1:
                    nx, ny = cx + 1, cy
                    if board[nx][ny] == 'x' and not visited[nx][ny]:
                        visited[nx][ny] = id
                        bottoms[ny] = max(bottoms[ny], nx)
                        nq.append((nx, ny))
                if cy > 0:
                    nx, ny = cx, cy - 1
                    if board[nx][ny] == 'x' and not visited[nx][ny]:
                        visited[nx][ny] = id
                        bottoms[ny] = max(bottoms[ny], nx)
                        nq.append((nx, ny))
                if cy < c - 1:
                    nx, ny = cx, cy + 1
                    if board[nx][ny] == 'x' and not visited[nx][ny]:
                        visited[nx][ny] = id
                        bottoms[ny] = max(bottoms[ny], nx)
                        nq.append((nx, ny))
            q = nq

        # 클러스터의 각 열의 바닥이 수직으로 떨어질 때의 거리중 최솟값을 구함
        min_fall = 100
        for i in range(c):
            # -1일 경우 해당 열에 미네랄 덩어리가 존재하지 않음
            if bottoms[i] == -1:
                continue

            fall = 0
            for j in range(bottoms[i]+1, r):
                if board[j][i] == '.':
                    fall += 1
                else:
                    break
            min_fall = min(min_fall, fall)

        if not min_fall:
            return False

        # 최소 낙하거리만큼 클러스터를 이동
        for i in range(c):
            if bottoms[i] == -1:
                continue
            for j in range(r-1, -1, -1):
                if board[j][i] == 'x' and visited[j][i] == id:
                    board[j][i] = '.'
                    board[j+min_fall][i] = 'x'

        return True

    # x, y의 미네랄이 부서졌을 때 클러스터의 이동 처리
    def process_cluster(x, y):
        visited = [[0] * c for _ in range(r)]
        # 미네랄이 부숴진 위치 기준 상하좌우로 나눠진 클러스터가 있는지 확인
        # 나눠진 클러스터가 바닥과 닿아있지 않다면 해당 클러스터의 이동을 처리
        if x > 0 and board[x-1][y] == 'x' and not visited[x-1][y]:
            if bfs(x-1, y, visited, 1):
                return
        if x < r-1 and board[x+1][y] == 'x' and not visited[x+1][y]:
            if bfs(x+1, y, visited, 2):
                return
        if y > 0 and board[x][y-1] == 'x' and not visited[x][y-1]:
            if bfs(x, y-1, visited, 3):
                return
        if y < c-1 and board[x][y+1] == 'x' and not visited[x][y+1]:
            if bfs(x, y+1, visited, 4):
                return

    input()
    rows = list(map(lambda x: r - int(x), input().split()))

    d = 1
    for row in rows:
        # 막대가 왼쪽에서 날아올 경우
        if d == 1:
            # 부숴질 미네랄 탐색
            for i in range(c):
                if board[row][i] == 'x':
                    board[row][i] = '.'
                    # 클러스터 이동 처리
                    process_cluster(row, i)
                    break

        # 막대가 오른쪽에서 날아올 경우
        else:
            # 부숴질 미네랄 탐색
            for i in range(c-1, -1, -1):
                if board[row][i] == 'x':
                    board[row][i] = '.'
                    # 클러스터 이동 처리
                    process_cluster(row, i)
                    break

        # 방향전환
        d *= -1

    return '\n'.join([''.join(board[i]) for i in range(r)])
