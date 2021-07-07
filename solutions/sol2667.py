import sys

input = sys.stdin.readline
n = int(input())
board = [input().rstrip() for _ in range(n)]
visit = [[0] * n for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# 2667 단지번호붙이기
# 격자형 지도에서 한덩어리 찾기 문제
# 전형적인 완전탐색 문제의 유형
def sol2667():
    cpx = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == '0' or visit[i][j] == 1:
                continue
            cpx.append(dfs(i, j))
    cpx.sort()
    print(len(cpx), '\n'.join(map(str, cpx)), sep='\n')


def dfs(i, j):
    visit[i][j] = 1
    res = 1
    for d in direction:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < n and 0 <= nj < n and not visit[ni][nj] and board[ni][nj] == '1':
            res += dfs(ni, nj)
    return res
