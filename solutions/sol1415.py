import sys
from collections import defaultdict

input = sys.stdin.readline


# 1415 사탕
# n개의 사탕을 조합하여 가격의 합이 소수가 되는 경우의 수를 구하는 문제
def sol1415():
    n = int(input())
    candies = defaultdict(int)
    for _ in range(n):
        candies[int(input())] += 1

    dp = defaultdict(int)
    dp[0] = 1
    for candy, cnt in candies.items():
        u = defaultdict(int)
        vals = [candy * i for i in range(1, cnt+1)]
        for v, c in dp.items():
            for val in vals:
                u[v + val] += c
        for v, c in u.items():
            dp[v] += c

    return sum([dp[i] for i in dp if is_prime(i)])


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**.5)+1):
        if not num % i:
            return False
    return True
