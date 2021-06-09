import sys

input = sys.stdin.readline


# 1152 단어의 개수
# 입력된 문장에 포함된 단어의 갯수를 구하는 문제
def sol1152():
    print(len(input().split()))
