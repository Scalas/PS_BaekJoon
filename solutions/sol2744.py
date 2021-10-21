import sys

input = sys.stdin.readline


# 2744 대소문자 바꾸기
# swapcase를 사용하여 간단히 해결가능
def sol2744():
    word = input().rstrip()
    return word.swapcase()
