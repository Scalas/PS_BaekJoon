import sys

input = sys.stdin.readline


# 기찍 N
def sol2742():
    print('\n'.join(map(str, range(int(input()), 0, -1))))