import sys

input = sys.stdin.readline


# 2902 KMP 는 왜 KMP 일까?
# 하이픈(-)으로 구분된 여러 이름들을 앞글자만 따서 만든 짧은이름을 구하는 문제
def sol2902():
    return ''.join([i[0] for i in input().split('-')])
