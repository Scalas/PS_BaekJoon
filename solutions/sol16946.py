import sys

input = sys.stdin.readline


# 16946 벽 부수고 이동하기 4
# n * m 격자공간에서 벽의 위치와 빈 공간의 위치가 주어지고
# 벽 중 하나를 각각 부순다음 벽을 부순 위치에서 이동 가능한 칸의 갯수를 구하는 문제
def sol16946():
    n, m = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(n)]
    idx = 2
    count = []

    # 빈 공간 클러스터들에게 각각 번호를 붙이고 각 클러스터의 크기를 구함
    def bfs(r, c, index):
        q = [(r, c)]
        board[r][c] = index
        cnt = 1
        while q:
            nq = []
            for cr, cc in q:
                if cr > 0:
                    nr, nc = cr - 1, cc
                    if not board[nr][nc]:
                        board[nr][nc] = index
                        nq.append((nr, nc))
                        cnt += 1
                if cr < n - 1:
                    nr, nc = cr + 1, cc
                    if not board[nr][nc]:
                        board[nr][nc] = index
                        nq.append((nr, nc))
                        cnt += 1
                if cc > 0:
                    nr, nc = cr, cc - 1
                    if not board[nr][nc]:
                        board[nr][nc] = index
                        nq.append((nr, nc))
                        cnt += 1
                if cc < m - 1:
                    nr, nc = cr, cc + 1
                    if not board[nr][nc]:
                        board[nr][nc] = index
                        nq.append((nr, nc))
                        cnt += 1
            q = nq
        count.append(cnt)

    for i in range(n):
        for j in range(m):
            if not board[i][j]:
                bfs(i, j, idx)
                idx += 1

    # 모든 벽마다 상하좌우로 인접한 빈공간 클러스터를 모두 구하여 그 크기를 더한 뒤
    # 벽이 있던 칸까지 1개를 추가하면 이동 가능한 칸의 갯수를 구할 수 있음
    answer = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                res = 1

                # 상하좌우로 인접한 칸중 같은 클러스터에 속한 칸이 있을 수 있기 때문에
                # set으로 인접한 클러스터 목록에서 중복을 제거
                cluster_set = set()
                if i > 0 and board[i - 1][j] > 1:
                    cluster_set.add(board[i - 1][j] - 2)
                if i < n - 1 and board[i + 1][j] > 1:
                    cluster_set.add(board[i + 1][j] - 2)
                if j > 0 and board[i][j - 1] > 1:
                    cluster_set.add(board[i][j - 1] - 2)
                if j < m - 1 and board[i][j + 1] > 1:
                    cluster_set.add(board[i][j + 1] - 2)
                for cluster in cluster_set:
                    res += count[cluster]

                # 인접한 클러스터들의 크기의 합 + 1 을 10으로 나눈 나머지를 정답 리스트에 저장
                answer[i][j] = res % 10

    return '\n'.join([''.join(map(str, answer[i])) for i in range(n)])
