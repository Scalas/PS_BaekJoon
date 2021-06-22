import sys


# 2609 최대공약수와 최소공배수
# 두 수의 최대공약수와 최소공배수를 구하는 문제
# 유클리드의 알고리즘을 사용하여 최대공약수를 구한 뒤 두 수의 곱에서 최대공약수를 나누면 최소공배수도 구할 수 있다
def sol2609():
    n, m = map(int, sys.stdin.read().split())
    if n < m:
        n, m = m, n
    gcd = [n, m]
    while gcd[1] != 0:
        gcd = [gcd[1], gcd[0] % gcd[1]]
    print(gcd[0], n * m // gcd[0], sep='\n')
