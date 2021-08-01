import sys

input = sys.stdin.readline


# 1644 소수의 연속합
# 연속한 소수를 합해서 n을 만들 수 있는 경우의 수를 구하는 문제
# n 까지의 소수의 리스트에서 투포인터를 통한 탐색을 수행하여 해결 가능하다
# 소수의 리스트는 에라토스테네스의 체를 사용하여 구한다
def sol1644():
    n = int(input())
    # n이 1인 경우 바로 0 반환
    if n == 1:
        return 0

    # 에라토스테네스의 체를 사용하여 n까지의 소수를 모두 구한다.
    isprime = [True] * (n + 1)
    isprime[0] = isprime[1] = False
    for i in range(2, int(n ** .5) + 1):
        if isprime[i]:
            isprime[2 * i::i] = [False] * (n // i - 1)
    primes = [i for i in range(2, n + 1) if isprime[i]]

    # 연속하는 소수 구간의 합이 n이라면 res += 1
    # n보다 작다면 끝부분 인덱스를 1 증가 / 크다면 시작부분 인덱스를 1 증가  구간의 합계를 갱신
    # 만약 시작과 끝의 인덱스를 이동했을 때 둘중 소수 리스트의 인덱스 범위를 넘어섰다면 break
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
