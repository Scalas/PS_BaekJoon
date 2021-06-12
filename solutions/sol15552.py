import sys

input = sys.stdin.readline


# 15552 빠른 A+B
def sol15552():
    print('\n'.join(map(str, [sum(map(int, i.split())) for i in sys.stdin.read().splitlines()[1:]])))
