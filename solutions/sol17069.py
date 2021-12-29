import sys

input = sys.stdin.readline


# 17069 파이프 옮기기 2
# n * n 격자공간에서 처음에 (0, 0), (0, 1) 을 차지하고있는 파이프를
# 45도씩 회전하여 한칸 앞으로 이동시킬 수 있을 때 파이프가 (n-1, n-1)에 도달하는 경우의 수
# 단, 파이프는 오른쪽, 우하단대각, 아래쪽으로만 이동할 수 있다.
def sol17069():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    # dp[i][j][k] 는 파이프의 한쪽이 (i, j) 로 이동할 수 있고
    # 방향이 k인 경우의 수
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

    # 초기상태
    dp[0][1][0] = 1

    for i in range(n):
        for j in range(n):
            # 파이프가 (i, j) 칸에 도달한 경우중 각각 방향이 가로, 세로, 대각선인 경우의 수
            h, v, d = dp[i][j]

            # 오른쪽으로 이동할 수 있는 경우(가로방향, 대각선방향)
            if j < n-1 and not board[i][j+1]:
                dp[i][j+1][0] += (h + d)

            # 아래쪽으로 이동할 수 있는 경우(세로방향, 대각선방향)
            if i < n-1 and not board[i+1][j]:
                dp[i+1][j][1] += (v + d)

            # 대각선 방향으로 이동할 수 있는 경우(모든 방향)
            if i < n-1 and j < n-1 and not (board[i][j+1] + board[i+1][j] + board[i+1][j+1]):
                dp[i+1][j+1][2] += (h + v + d)

    # (n-1, n-1)에 도달하는 모든 경우의 수 반환
    return sum(dp[-1][-1])
