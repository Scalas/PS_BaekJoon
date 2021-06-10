import sys

input = sys.stdin.readline


# 10818 최소, 최대
# 리스트의 최소, 최대값을 구하는 문제
def sol10818():
    input()
    nums = list(map(int, input().split()))
    print(min(nums), max(nums))
