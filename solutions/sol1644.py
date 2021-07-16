import sys

input = sys.stdin.readline


# 1644 소수의 연속합
# 연속한 소수를 합해서 n을 만들 수 있는 경우의 수를 구하는 문제
# n 까지의 소수의 리스트에서 투포인터를 통한 탐색을 수행하여 해결 가능하다
# 소수의 리스트는 에라토스테네스의 체를 사용하여 구한다
def sol1644():
    n = int(input())
    if n == 1:
        return 0

    isprime = [True] * (n + 1)
    isprime[0] = isprime[1] = False
    for i in range(2, int(n ** .5) + 1):
        if isprime[i]:
            isprime[2 * i::i] = [False] * (n // i - 1)
    primes = [i for i in range(2, n + 1) if isprime[i]]
    l, s = 0, 0
    answer = 0
    for r in range(len(primes)):
        s += primes[r]
        if s < n:
            continue
        while s >= n:
            if s == n:
                answer += 1
            s -= primes[l]
            l += 1

    return answer
