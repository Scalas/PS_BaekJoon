import sys

input = sys.stdin.readline
mod = 1000000007


# 11444 피보나치 수 6
# n 번째 피보나치 수를 구하는 문제
# n의 범위가 굉장히 크기때문에 O(N)으로는 풀 수 없다
# 피보나치 수는 앞의 두 수를 더하는 것이기 때문에 행렬의 곱을 활용하여 풀 수 있다
# 1*2 행렬 [[f1, f2]] 에 2*2 행렬 [[0, 1], [1, 1]] 을 곱하면
# [[f1, f2]]를 얻을 수 있다
# 즉, fn은 행렬 ([[0, 1]] * ([[0, 1], [1, 1]]) ^ (n-1))의 두 번째 요소가 된다
def sol11444():
    n = int(input())
    if n == 1:
        print(1)
        return
    fibo = [[0, 1]]
    mat = [[0, 1], [1, 1]]
    fibo = matmul(fibo, matsq(mat, n - 1))
    print(fibo[0][1])


def matmul(a, b):
    r, c, m = len(a), len(b[0]), len(b)
    b = list(zip(*b))
    return [[sum([i * j for i, j in zip(a[row], b[col])]) % mod for col in range(c)] for row in range(r)]


def matsq(m, x):
    if x == 1:
        return m
    res = matsq(m, x//2)
    res = matmul(res, res)
    if x % 2:
        res = matmul(res, m)
    return res
