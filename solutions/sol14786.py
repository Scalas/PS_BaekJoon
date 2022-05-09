import sys
from math import sin

input = sys.stdin.readline


# 14786 Ax + Bsin(x) = C
# A, B, C 세 정수가 주어졌을 때 Ax + Bsin(x) + C를 만족하는 x값을 구하는 문제
def sol14786():
    a, b, c = map(int, input().split())
    s = (c - b) / a
    e = (b + c) / a
    while s < e:
        m = (s + e) / 2
        res = round(a * m + b * sin(m), 9)
        if res > c:
            e = m
        elif res < c:
            s = m
        else:
            return m
