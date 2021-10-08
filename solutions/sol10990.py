import sys

input = sys.stdin.readline


# 10990 별 찍기 - 15
# 규칙에 따라 *을 출력하는 문제
def sol10990():
    n = int(input())
    buffer = [[' '] * (2 * n - 1) for _ in range(n)]
    idx = n - 1
    for i in range(n):
        buffer[i][idx + i] = '*'
        buffer[i][idx - i] = '*'

    return '\n'.join([''.join(buffer[i]).rstrip() for i in range(n)])
