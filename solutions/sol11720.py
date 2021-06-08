import sys

input = sys.stdin.readline


# 11720 숫자의 합
# 공백없이 입력된 숫자를 한자리단위로 끊어서 모두 더한 값을 구하는 문제
def sol11720():
    input()
    print(sum(map(int, input().rstrip())))
