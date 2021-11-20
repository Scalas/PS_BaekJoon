import sys

input = sys.stdin.readline


# 16395 파스칼의 삼각형
# 파스칼의 삼각형의 n행 k열의 수를 구하는 문제
# 이항계수 C(n-1, k-1)과 같음
def sol16395():
    n, k = map(int, input().split())
    n -= 1
    k -= 1
    if k > n-k:
        k = n-k
    u, d = 1, 1
    for i in range(1, k+1):
        u *= (n+1-i)
        d *= i
    return u//d
