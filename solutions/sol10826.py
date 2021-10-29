import sys

input = sys.stdin.readline


# 10826 피보나치 수 4
# 동적계획법으로 간단히 해결가능
def sol10826():
    n = int(input())
    fibo = [0, 1]

    if n <= 1:
        return fibo[n]

    for _ in range(n-1):
        fibo = fibo[1], fibo[0]+fibo[1]

    return fibo[1]
