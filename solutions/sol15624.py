import sys

input = sys.stdin.readline
MOD = 1000000007
fm = [[0, 1], [1, 1]]


# 8394 피보나치 수 7
# n번째 피보나치 수를 구하는 문제
def sol8394():
    n = int(input())
    # n이 1 이하일 때
    if n <= 1:
        return n

    # 행렬의 빠른 제곱을 활용하여 n번째 피보나치 수를 구한다
    fibo = [[0, 1]]
    return mat_mul(fibo, mat_sq(fm, n-1))[0][1]


# 행렬 a와 b의 곱셈
def mat_mul(a, b):
    r, m, c = len(a), len(b), len(b[0])
    res = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for k in range(m):
                res[i][j] += (a[i][k] * b[k][j]) % MOD
            res[i][j] %= MOD
    return res


# 행렬 m의 d제곱
def mat_sq(m, d):
    if d == 1:
        return m
    mid = d // 2
    sqr = mat_sq(m, mid)
    res = mat_mul(sqr, sqr)
    if d % 2:
        res = mat_mul(res, fm)
    return res
