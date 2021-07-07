import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# 1012 유기농 배추
# 상하좌우로 인접하게 심어진 배추를 하나의 밭으로 볼떄 밭의 갯수를 구하는 문제
# 전형적인 dfs 문제
def sol1012():
    answer = []
    for t in range(int(input())):
        m, n, k = map(int, input().split())
        board = [[0] * m for _ in range(n)]
        visit = [[0] * m for _ in range(n)]
        for c, r in [map(int, input().split()) for _ in range(k)]:
            board[r][c] = 1

        res = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1 and not visit[i][j]:
                    dfs(board, visit, n, m, i, j)
                    res += 1
        answer.append(str(res))
    print('\n'.join(answer))


def dfs(board, visit, n, m, i, j):
    visit[i][j] = 1

    for d in direction:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 1 and not visit[ni][nj]:
            dfs(board, visit, n, m, ni, nj)
