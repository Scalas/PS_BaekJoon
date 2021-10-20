import sys

input = sys.stdin.readline


# 10164 격자상의 경로
# (1, 1) 에서 (n, m) 으로 우측 또는 하단으로만 이동하여 도달하는 경로의 갯수를 구하는 문제
# k가 0이 아닐 경우 k번 칸을 반드시 지나야한다. k번 칸의 좌표를 구하는 방법에 주의
def sol10164():
    n, m, k = map(int, input().split())
    board = [[0] * (m+1) for _ in range(n+1)]
    mr, mc = k // m + 1, k % m
    if not mc:
        mr -= 1
        mc = m
    board[1][1] = 1
    for diag in range(3, n+m+1):
        for i in range(max(diag-m, 1), min(diag, n+1)):
            j = diag-i
            board[i][j] = board[i-1][j] + board[i][j-1]

    return board[-1][-1] if not k else board[mr][mc] * board[n-mr+1][m-mc+1]
