import sys

input = sys.stdin.readline


# 10829 이진수 변환
# 주어진 10진수를 2진수로 변환하는 문제
def sol10829():
    return bin(int(input()))[2:]
