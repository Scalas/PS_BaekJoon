import sys

input = sys.stdin.readline


# 11726 2xn 타일링
# 2 x n 의 직사각형을 1 x 2, 2 x 1 타일로 채우는 방법의 수를 구하는 문제
# 2 x (n-1) 직사각형을 채운 상태에서 1 x 2 타일을 추가하는 경우와
# 2 x (n-2) 직사각형을 채운 상태에서 2 x 1 타일 두 개를 추가하는 경우
# dp[n] = dp[n-1] + dp[n-2] 가 성립한다.
def sol11726():
    n = int(input())
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 10007
