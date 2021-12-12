import sys

input = sys.stdin.readline


# 2526 싸이클
# 주어진 n, p에 대해서 n에서 시작하여 n을 곱하고 p로 나눈 나머지를 구하는 연산을 반복
# 결과값이 순환하는 구간의 크기를 구하는 문제
def sol2526():
    n, p = map(int, input().split())
    idx = [0] * 100

    if n < p:
        idx[n] = 0
    i = 1
    num = (n * n) % p
    while not idx[num]:
        idx[num] = i
        num = (num * n) % p
        i += 1
    return i - idx[num]
