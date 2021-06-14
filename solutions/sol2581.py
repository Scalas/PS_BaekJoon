import sys
import math

input = sys.stdin.read


# 2581 소수
# m 부터 n 까지의 수 중에서 소수인 것들의 합과 그 중 최소값을 구하는 문제
def sol2581():
    m, n = map(int, input().split())
    ps = 0
    pm = 0
    for num in range(n, m-1, -1):
        if isPrime(num):
            ps += num
            pm = num
    if ps==0:
        print(-1)
    else:
        print(ps, pm, sep='\n')


def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if (n % i == 0):
            return False
    return True
