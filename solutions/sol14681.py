import sys

input = sys.stdin.read


# 14681 사분면고르기
def sol14681():
    x, y = map(int, input().split())
    if x * y > 0:
        print(1 if x > 0 else 3)
    else:
        print(2 if x < 0 else 4)
