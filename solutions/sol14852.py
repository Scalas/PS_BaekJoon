import sys

input = sys.stdin.readline
MOD = 1000000007


# 14852 타일 채우기 3
# 2 * n 크기의 벽을 2 * 1, 1 * 2, 1 * 1 의 타일로 채우는 경우의 수를 구하는 문제
def sol14852():
    n = int(input())
    dp = [1, 2]
    sum_val = 3
    for i in range(2, n+1):
        res = (sum_val * 2 + dp[-2]) % MOD
        dp.append(res)
        sum_val = (sum_val + res) % MOD

    return dp[n]
