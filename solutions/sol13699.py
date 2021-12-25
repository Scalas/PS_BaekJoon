import sys

input = sys.stdin.readline


# 13699 점화식
# dp[n] = dp[0] * dp[n-1] + dp[1] * dp[n-2] * ... * dp[n-1] * dp[0] 이고 dp[0] = 1일 때
# dp[n] 을 구하는 문제
def sol13699():
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n+1):
        m = i // 2
        dp[i] = sum([dp[j] * dp[i-j-1] for j in range(m)]) * 2
        if i % 2:
            dp[i] += dp[m] ** 2
    return dp[-1]
