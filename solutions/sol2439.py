import sys

input = sys.stdin.readline


# 2439 별 찍기 - 2
def sol2439():
    n = int(input())
    answer = [' ' * (n-i) + '*' * i for i in range(1, n+1)]
    print('\n'.join(answer))
