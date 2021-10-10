import sys

input = sys.stdin.readline


# 2163 초콜릿 자르기
def sol2163():
    n, m = map(int, input().split())
    return n * m - 1
