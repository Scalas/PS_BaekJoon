import sys

input = sys.stdin.readline


# 2741 N 찍기
def sol2741():
    print('\n'.join(map(str, range(1, int(input())+1))))
