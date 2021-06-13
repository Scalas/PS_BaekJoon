import sys

input = sys.stdin.readline


# 10869 사칙연산
def sol10869():
    a, b = map(int, input().split())
    print('\n'.join(map(str, [a + b, a - b, a * b, a // b, a % b])))

