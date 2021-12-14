import sys

input = sys.stdin.readline


# 13752 히스토그램
# 각 행에 주어진 숫자만큼 =를 출력하는 문제
def sol13752():
    return '\n'.join(['=' * int(input()) for _ in range(int(input()))])
