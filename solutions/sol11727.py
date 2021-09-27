import sys

input = sys.stdin.readline


# 11727 2xn 타일링 2
# 2 x n 의 직사각형을 1 x 2, 2 x 1, 2 x 2 타일로 채우는 방법의 수를 구하는 문제
# 2 x (n-1) 직사각형을 채운 상태에서 1 x 2 타일을 추가하는 한 가지 경우와
# 2 x (n-2) 직사각형을 채운 상태에서 2 x 1 타일 두개 또는 2 x 2 타일 하나를 추가하는 두 가지 경우
# dp[n] = dp[n-1] + dp[n-2] * 2 가 성립한다.
def sol11727():
    n = int(input())
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007

    return dp[n]
