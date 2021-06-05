import sys

input = sys.stdin.readline
dp = {}


# 10870 피보나치
# 재귀함수를 활용하여 피보나치 수를 구하는 문제
# 캐싱을 통해 중복계산을 줄일 수 있다
def sol10870():
    print(fibo(int(input())))


def fibo(n):
    if (n <= 1):
        return n
    if not dp.get(n):
        dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n]
