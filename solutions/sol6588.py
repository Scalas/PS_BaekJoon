import sys

input = sys.stdin.readline


# 6588 골드바흐의 추측
# 4보다 큰 짝수를 두 홀수인 소수의 합으로 나타낼 수 있는지 6이상 100만 이하의 짝수에 대해 검증하는 문제
# 에라토스테네스의 체를 사용하거나 n의 제곱근까지만 약수 검사를 하는것으로 해결 가능하다.
def sol6588():
    N_MAX = 1000000
    eratos = [True] * (N_MAX + 1)
    eratos[0] = eratos[1] = False
    for i in range(2, N_MAX // 2 + 1):
        eratos[2 * i:N_MAX + 1:i] = [False] * (N_MAX // i - 1)
    primes = [i for i in range(2, N_MAX + 1) if eratos[i]]

    answer = []
    while True:
        n = int(input())
        if n == 0:
            break
        for prime in primes:
            if prime > n:
                answer.append('Goldbach\'s conjecture is wrong')
                break
            elif eratos[n - prime]:
                answer.append('%d = %d + %d' % (n, prime, n - prime))
                break

    return '\n'.join(answer)
