import sys

input = sys.stdin.readline


# 10822 더하기
# 주어진 수를 모두 더한 값을 구하는 문제
def sol10822():
    return sum(map(int, input().split(',')))
