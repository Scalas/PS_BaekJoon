import sys

input = sys.stdin.readline


# 2438 별 찍기 - 1
def sol2438():
    answer = ['*'*n for n in range(1, int(input())+1)]
    print('\n'.join(answer))
