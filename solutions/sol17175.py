import sys

input = sys.stdin.readline


# 17175 피보나치는 지겨웡~
# n에 대해 재귀함수로 구현된 피보나치 함수를 호출했을 때
# 피보나치 함수가 호출되는 횟수를 구하는 문제
def sol17175():
    n = int(input())
    dp = [1, 1]
    for _ in range(n-1):
        dp.append((dp[-1] + dp[-2] + 1) % 1000000007)

    return dp[n]
