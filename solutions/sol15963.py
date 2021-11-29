import sys

input = sys.stdin.readline


# 15963 CASIO
# 두 수의 동일 여부를 판단하는 문제
def sol15963():
    u, v = map(int, input().split())
    return 1 if u == v else 0
