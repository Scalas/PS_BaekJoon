import sys

input = sys.stdin.readline


# 10430 나머지
def sol10430():
    a, b, c = map(int, input().split())
    print('\n'.join(map(str, [(a + b) % c, ((a % c) + (b % c)) % c, (a * b) % c,  ((a % c) * (b % c)) % c])))
