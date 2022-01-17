import sys

input = sys.stdin.readline
fm = [[0, 1], [1, 1]]


# 8394 악수
# 일렬로 앉아있는 n명의 사람이 인접한 좌측 혹은 우측사람중 한쪽과 악수를 할 수 있을 때
# 악수를 하는 모든 경우의 수를 구하는 문제
def sol8394():
    n = int(input())
    # 3명 이하의 사람이 악수를 하는 경우의 수
    if n <= 3:
        return n

    # n명의 사람이 악수를 하는 경우의 수는 마지막 두사람이 악수를 하는 경우의 수와
    # 악수를 하지 않는 경우의 수를 더한 값과 같다. (dp[n] = dp[n-2] + dp[n-1])
    # 즉, n번째 피보나치 수의 마지막 자릿수를 구하는 문제가 된다.
    # n이 최대 1000만으로 매우 크기 때문에 행렬의 빠른 제곱을 사용하여
    # O(logN)으로 피보나치 행렬 [[0, 1], [1, 1]]의 n-3제곱을 구하고
    # fibonacci(2), fibonacci(3)의 값을 가진 fibo 행렬에 피보나치 행렬을 곱하여
    # fibonacci(n-1), fibonacci(n)의 값을 구한다.
    fibo = [[2, 3]]
    return mat_mul(fibo, mat_sq(fm, n-3))[0][1]


# 행렬 a와 b의 곱셈
def mat_mul(a, b):
    r, m, c = len(a), len(b), len(b[0])
    res = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for k in range(m):
                res[i][j] += (a[i][k] * b[k][j]) % 10
            res[i][j] %= 10
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
