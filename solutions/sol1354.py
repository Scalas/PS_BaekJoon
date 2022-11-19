import sys
from math import floor

input = sys.stdin.readline


# 1354 무한 수열 2
# n, p, q, x, y 가 주어졌을 때 수열 A의 n 번째 값을 구하는 문제
# 수열 A(i)는 i가 0 이하일 경우에는 1이며
# 그 외의 경우에는 A(i / p - x) + A(i / q - y) 이다 (계산된 인덱스는 소숫점을 버림한다.)
def sol1354():
    n, p, q, x, y = map(int, input().split())
    dp = dict()

    def A(idx):
        if idx <= 0:
            return 1
        if dp.get(idx, -1) == -1:
            dp[idx] = A(floor(idx / p - x)) + A(floor(idx / q - y))
        return dp[idx]

    return A(n)
