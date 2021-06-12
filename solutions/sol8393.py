import sys

input = sys.stdin.readline


# 8393 합
def sol8393():
    n = int(input())
    print(n*(n+1)//2)
