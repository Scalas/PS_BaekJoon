import sys

input = sys.stdin.readline
INF = float('inf')
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# 1261 알고스팟
# m * n 격자공간의 미로가 주어졌을 때(빈공간 0 | 벽 1)
# (0, 0)에서 출발하여 (m-1, n-1) 에 도착하기 위해 부숴야할 벽의 최소갯수를 구하는 문제
def sol1261():
    n, m = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(m)]

    # dp[i][j] 는 (0, 0)에서 (i, j) 로 가기위해 부숴야할 벽의 최소갯수
    dp = [[INF] * (n+1) for _ in range(m)]

    # (0, 0)에서 출발
    q = [(0, 0)]

    # (0, 0)은 항상 빈공간이므로 부숴야할 벽의 수는 0
    dp[0][0] = 0

    while q:
        nq = []
        for r, c in q:
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    # 현재까지 부순 벽의 갯수 + 도착할 위치(nr, nc)의 벽의 갯수(0 or 1)이
                    # dp[nr][nc]보다 적다면 dp 값을 갱신하고 (nr, nc)를 큐에 삽입
                    cnt = dp[r][c] + board[r][c]
                    if cnt < dp[nr][nc]:
                        dp[nr][nc] = cnt
                        nq.append((nr, nc))
        q = nq
    
    # (m-1, n-1)에 도달하기 위해 부숴야할 벽의 최소갯수를 반환
    return dp[m-1][n-1]
