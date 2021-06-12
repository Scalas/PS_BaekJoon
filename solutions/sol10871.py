import sys

input = sys.stdin.readline


# 10871 X보다 작은 수
def sol10871():
    n, x = map(int, input().split())
    print(' '.join(map(str, [num for num in input().split() if int(num)<x])))

