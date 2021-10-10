import sys

input = sys.stdin.readline


# 10953 A + B - 6
def sol10953():
    return '\n'.join(map(str, [sum(map(int, input().split(','))) for _ in range(int(input()))]))
