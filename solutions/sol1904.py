import sys

input = sys.stdin.readline
mod = 15746


# 1904 01타일
# 00과 1 두종류의 타일로 n자리 이진수열을 만드는 경우의 수 구 하기
# n자리 수열을 만드는 방법은 n-1자리에 1을 추가하거나 n-2자리에 00을 추가하는 두가지가 있다
# 그러므로 tile[n] = tile[n-1] + tile[n-2]가 된다. 즉, n+1번쨰 피보나치 수열을 구하는 문제가 된다


# 첫 번째 시도
# 단순히 동적계획법을 사용해서 구하는 방식
# 이 방법도 충분히 빠르기때문에 문제를 푸는데 문제는 없다
def sol1904():
    d1, d2 = 1, 2
    n = int(input())
    if n < 3:
        print(n)
    else:
        for _ in range(n-2):
            d1, d2 = d2, (d1 + d2) % mod
        print(d2)


# 두 번째 시도
# 피보나치 수열은 행렬의 제곱으로 더 빠르게 구할 수 있다
# 빠른 행렬의 제곱을 응용하면 O(logN)의 시간으로 해결 가능하다
def sol1904_2():
    print(tile(int(input())))


def tile(n):
    if n <= 3:
        return n

    dp = (2, 3)
    m = matsq((0, 1, 1, 1), n - 3)
    return (dp[0] * m[1] + dp[1] * m[3]) % mod


def matmul(a, b):
    return ((a[0] * b[0] + a[1] * b[2]) % mod,
            (a[0] * b[1] + a[1] * b[3]) % mod,
            (a[2] * b[0] + a[3] * b[2]) % mod,
            (a[2] * b[1] + a[3] * b[3]) % mod
            )


def matsq(a, n):
    if n == 1:
        return a
    m = n // 2
    res = matsq(a, m)
    res = matmul(res, res)
    if n % 2 != 0:
        res = matmul(res, a)
    return res
