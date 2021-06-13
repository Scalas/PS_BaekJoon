import sys

input = sys.stdin.read


# 2588 곱셈
def sol2588():
    a, b = map(int, input().split())
    print('\n'.join(map(str, [a * (b % 10), a * (b // 10 % 10), a * (b // 100 % 10), a * b])))
