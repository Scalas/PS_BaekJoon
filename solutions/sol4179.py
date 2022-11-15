import sys

input = sys.stdin.readline


# 4179 불!
# n * m 격자공간에 불(F)과 지훈(J)이 있고
# 불은 매 시간마다 인접한 상하좌우로 퍼져나가며
# 지훈은 같은 시간에 불이 퍼진곳으로는 이동하지 못한다고 할때
# 지훈이 미로를 빠져나갈 수 있는 최단시간을 구하는 문제
# 단, 미로를 빠져나가려면 미로의 가장자리에서 한칸을 더 가야하며 
# 불도 지훈도 벽이 있는 곳으로는 이동 불가능하다
def sol4179():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    q = []
    fire = []
    dp = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'J':
                q.append((i, j))
            elif board[i][j] == 'F':
                fire.append((i, j))
                dp[i][j] = 0

    # 각 칸에 불이 퍼져나가는 시간을 미리 기록
    turn = 0
    while fire:
        turn += 1
        nfire = []
        for r, c in fire:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if board[nr][nc] == '#':
                    continue
                if dp[nr][nc] < 0:
                    dp[nr][nc] = turn
                    nfire.append((nr, nc))
        fire = nfire

    # 지훈이 각 칸에 불이 퍼지는 시간 이전에만 이동 가능하도록 하여
    # 가장 빨리 가장자리에 도달하는 시간 + 1 을 구한다.
    turn = 0
    visited = [[False] * m for _ in range(n)]
    visited[q[0][0]][q[0][1]] = True
    while q:
        turn += 1
        nq = []
        for r, c in q:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    return turn
                if board[nr][nc] == '#':
                    continue
                if 0 <= dp[nr][nc] <= turn:
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = True
                nq.append((nr, nc))
        q = nq

    return 'IMPOSSIBLE'
