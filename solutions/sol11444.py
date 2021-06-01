import sys

input = sys.stdin.readline
MOD = 1000000007


# 11444 피보나치 수 6
# n 번째 피보나치 수를 구하는 문제
# n의 범위가 굉장히 크기때문에 O(N)으로는 풀 수 없다
# 피보나치 수는 앞의 두 수를 더하는 것이기 때문에 행렬의 곱을 활용하여 풀 수 있다
# 1*2 행렬 [[f1, f2]] 에 2*2 행렬 [[0, 1], [1, 1]] 을 곱하면
# [[f1, f2]]를 얻을 수 있다
# 즉, fn은 행렬 ([[0, 1]] * ([[0, 1], [1, 1]]) ^ (n-1))의 두 번째 요소가 된다
def sol11444():
    global MOD

    n = int(input())
    print(fibo(n) % MOD)


def fibo(n):
    if (n <= 1):
        return n
    start = [[0, 1]]
    base = [[0, 1], [1, 1]]
    base = matsq(base, n - 1)
    res = matmult(start, base)
    return res[0][1]


def matmult(a, b):
    global mod

    r, c = len(a), len(b[0])
    m = len(a[0])
    ret = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for k in range(m):
                ret[i][j] += a[i][k] * b[k][j]
                ret[i][j] %= MOD
    return ret


def matsq(a, b):
    if (b == 1):
        return a
    ret = matsq(a, b // 2)
    ret = matmult(ret, ret)
    if (b % 2 != 0):
        ret = matmult(ret, a)
    return ret
