import sys


# 11399 ATM
# 대기시간의 합을 최소화하는 문제
def sol11399():
    n, *p = map(int, sys.stdin.read().split())
    p.sort()
    count = list(range(n, 0, -1))
    print(sum([p[i] * count[i] for i in range(n)]))
