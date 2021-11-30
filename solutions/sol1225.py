import sys

input = sys.stdin.readline


# 1225 이상한 곱셈
# a와 b의 각 자릿수끼리의 카르테시안 곱의 합을 구하는 문제
# 두 수의 자릿수의 총합을 서로 곱하여 구할 수 있다.
def sol1225():
    a, b = map(lambda x:sum(map(int, list(x))), input().split())

    return a * b
