import sys

input = sys.stdin.readline


# 1330 두 수 비교하기
def sol1330():
    a, b = map(int, input().split())
    print('>' if a>b else '<' if a<b else '==')
