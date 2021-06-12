import sys

input = sys.stdin.readline


# 11021 A+B - 7
def sol11021():
    print('\n'.join([f'Case #{idx+1}: {s}' for idx, s in enumerate([sum(map(int, i.split())) for i in sys.stdin.read().splitlines()[1:]])]))
