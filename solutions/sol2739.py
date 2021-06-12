import sys

input = sys.stdin.readline


# 2739 구구단
def sol2739():
    n = int(input())
    answer = []
    for i in range(1, 10):
        answer.append(f'{n} * {i} = {n * i}')
    print('\n'.join(answer))
