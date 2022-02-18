import sys

input = sys.stdin.readline
mod = 100000


# 5569 출근 경로
# (1, 1)에서 출발하여 (w, h)에 도달하는 모든 경로의 수를 구하는 문제
# 단, 위쪽 혹은 오른쪽으로만 이동 가능하며 방향전환시 두칸이상 움직여야 다시 방향전환이 가능
def sol5569():
    w, h = map(int, input().split())

    # dp[i][j][k] 는 (i, j)에 있고 상태(방향, 방향전환 가능여부)가 k인 경우의 수
    # 0 : 행 방향, 방향전환 가능
    # 1 : 행 방향, 방향전환 불가
    # 2 : 열 방향, 방향전환 가능
    # 3 : 열 방향, 방향전환 불가
    dp = [[[0] * 4 for _ in range(w)] for _ in range(h)]

    for i in range(1, h):
        dp[i][0][0] = 1
    for j in range(1, w):
        dp[0][j][2] = 1

    for i in range(1, h):
        for j in range(1, w):
            for k in range(4):
                # 방향을 바꾸지 않을 경우
                # 행방향
                if k == 0:
                    dp[i][j][k] = (dp[i-1][j][0] + dp[i-1][j][1]) % mod
                # 열방향
                elif k == 2:
                    dp[i][j][k] = (dp[i][j-1][2] + dp[i][j-1][3]) % mod

                # 방향을 바꿀 경우
                else:
                    dp[i][j][k] = dp[i-1][j][2] if k == 1 else dp[i][j-1][0]

    return sum(dp[-1][-1]) % mod
