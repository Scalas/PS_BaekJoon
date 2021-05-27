import sys

input = sys.stdin.readline


def sol1037():
    input()
    div = list(map(int, input().split()))
    div.sort()
    print(div[0]*div[-1])