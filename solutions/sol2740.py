import sys

input = sys.stdin.readline


# 2740행렬 곱셈
# 두 행렬의 곱을 구하는 문제
def sol2740():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    m, k = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(m)]

    answer = [' '.join(map(str, line)) for line in matmult(a, b)]
    print('\n'.join(answer))


def matmult(a, b):
    r, c, m = len(a), len(b[0]), len(b)
    res = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for k in range(m):
                res[i][j] += a[i][k] * b[k][j]
    return res
