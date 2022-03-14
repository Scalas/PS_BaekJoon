import sys

sys.setrecursionlimit(10001)
input = sys.stdin.readline


# 2146 다리 만들기
# n * n 격자지도상에 육지는 1, 바다는 0으로 표시되며
# 상하좌우로 이어져있는 육지를 섬이라고 부른다.
# 지도상의 모든 섬들 중 두 섬의 사이를 잇는 다리를 건설하려할 때
# 건설가능한 다리의 최소길이를 구하는 문제
def sol2146():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 방문여부 체크
    visited = [[False] * n for _ in range(n)]

    # 섬의 경계선
    borderline = []

    def dfs(r, c, k):
        visited[r][c] = True
        check = False
        # 상, 하, 좌, 우에 대해 이어진 육지가 있는지 확인하고
        # 육지가 이어져있다면 dfs를 재귀호출, 바다와 이어진다면 check를 True로 하여
        # 섬의 경계선에 있는 육지임을 표시
        if r > 0:
            nr, nc = r-1, c
            if board[nr][nc]:
                if not visited[nr][nc]:
                    dfs(nr, nc, k)
            else:
                check = True
        if r < n-1:
            nr, nc = r+1, c
            if board[nr][nc]:
                if not visited[nr][nc]:
                    dfs(nr, nc, k)
            else:
                check = True
        if c > 0:
            nr, nc = r, c-1
            if board[nr][nc]:
                if not visited[nr][nc]:
                    dfs(nr, nc, k)
            else:
                check = True
        if c < n-1:
            nr, nc = r, c+1
            if board[nr][nc]:
                if not visited[nr][nc]:
                    dfs(nr, nc, k)
            else:
                check = True

        # 섬의 경계선임을 표시하기 위해 k로 표시하고 borderline에 좌표를 삽입
        if check:
            board[r][c] = k
            borderline.append((r, c))

    # 섬의 경계 구분번호는 2부터 시작(육지 1과 구분)
    idx = 2
    # 각 섬마다 경계선상에 구분번호를 표시하고 경계선 좌표리스트를 작성
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j]:
                dfs(i, j, idx)
                idx += 1

    # 다리의 최소길이
    answer = 10 ** 5

    # 섬의 경계의 좌표들로부터 시작하여 처음으로 다른 섬의 경계에 닿을 때 까지
    # bfs로 탐색하여 각 경계로부터의 다리의 최소길이중 최솟값을 구하여 반환
    for r, c in borderline:
        visited = [[False] * n for _ in range(n)]
        q = [(r, c)]
        visited[r][c] = True
        cnt = 0
        check = False
        while q:
            nq = []
            for cr, cc in q:
                if cr > 0:
                    nr, nc = cr-1, cc
                    if not board[nr][nc] and not visited[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                    elif board[nr][nc] > 1 and board[nr][nc] != board[r][c]:
                        check = True
                        break
                if cr < n-1:
                    nr, nc = cr+1, cc
                    if not board[nr][nc] and not visited[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                    elif board[nr][nc] > 1 and board[nr][nc] != board[r][c]:
                        check = True
                        break
                if cc > 0:
                    nr, nc = cr, cc-1
                    if not board[nr][nc] and not visited[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                    elif board[nr][nc] > 1 and board[nr][nc] != board[r][c]:
                        check = True
                        break
                if cc < n-1:
                    nr, nc = cr, cc+1
                    if not board[nr][nc] and not visited[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                    elif board[nr][nc] > 1 and board[nr][nc] != board[r][c]:
                        check = True
                        break
            if check:
                break
            q = nq
            cnt += 1
        answer = min(answer, cnt)
    return answer
