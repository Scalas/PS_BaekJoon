import sys

input = sys.stdin.read


# 9461 파도반 수열
# 수열의 n번째 값을 구하는 문제
def sol9461():
    dp = [1] * 100
    dp[3] = dp[4] = 2
    for i in range(5, 100):
        dp[i] = dp[i - 1] + dp[i - 5]
    _, *case = map(int, input().split())
    print('\n'.join([str(dp[i - 1]) for i in case]))