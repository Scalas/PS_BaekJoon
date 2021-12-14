import sys

input = sys.stdin.readline


# 8320 직사각형을 만드는 방법
# 1*1 정사각형 n개로 만들 수 있는 직사각형의 갯수를 구하는 문제
def sol8320():
    n = int(input())
    return sum([n // i - i + 1 for i in range(1, int(n**.5)+1)])
