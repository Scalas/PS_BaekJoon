import sys

input = sys.stdin.readline


# 14495 피보나치
# f[n] = f[n-1] + f[n-3] 인 유사 피보나치 수열의 n번째 수를 구하는 문제
def sol14495():
    n = int(input())
    dp = [0, 1, 1, 1]
    for _ in range(4, n+1):
        dp.append(dp[-1] + dp[-3])
    return dp[n]
