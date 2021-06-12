import sys

input = sys.stdin.readline


# 2753 윤년
def sol2753():
    n = int(input())
    if n % 4 == 0:
        if n % 100 == 0:
            print(1 if n % 400 == 0 else 0)
        else:
            print(1)
    else:
        print(0)

