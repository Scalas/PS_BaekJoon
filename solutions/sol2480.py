import sys

input = sys.stdin.readline


# 2480 주사위 세개
# 주사위 눈의 값 세개가 주어졌을 때 규칙에따라 상금을 구하는 문제
def sol2480():
    a, b, c = map(int, input().split())
    if a == b == c:
        return a * 1000 + 10000
    elif a == b or a == c:
        return a * 100 + 1000
    elif b == c:
        return b * 100 + 1000
    else:
        return max(a, b, c) * 100
