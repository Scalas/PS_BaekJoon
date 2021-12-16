import sys

input = sys.stdin.readline


# 1252 이진수 덧셈
# 두 이진수를 더한 결과를 구하는문제
def sol1252():
    return bin(sum(map(lambda x:int(x, 2), input().split())))[2:]
