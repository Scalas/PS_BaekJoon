import sys

input = sys.stdin.readline


# 2884 알람 시계
def sol2884():
    h, m = map(int, input().split())
    t = h * 60 + m - 45
    if t < 0:
        t += 60*24
    print(t//60, t%60)
