import sys

input = sys.stdin.readline


# 3908 서로 다른 소수의 합
def sol3908():
    # 1120 이하의 소수 리스트를 구함
    is_prime = [True] * 1121
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, 1121):
        if is_prime[i]:
            primes.append(i)
            is_prime[i * 2:1121:i] = [False] * (1120 // i - 1)
    pn = len(primes)

    # 만들어야할 숫자가 i, 사용해야할 서로다른 소수의 수가 j, k번째 소수부터는 쓸 수 없을 때
    # dp[i][j][k] 는 숫자 i를 만들 수 있는 경우의 수
    dp = [[[-1] * 188 for _ in range(15)] for _ in range(1121)]

    def dfs(remain, count, last):
        if not count:
            return 0 if remain else 1
        if remain < 2:
            return 0
        if dp[remain][count][last] == -1:
            res = 0
            for i in range(last):
                prime = primes[i]
                if prime <= remain:
                    res += dfs(remain - prime, count - 1, i)
            dp[remain][count][last] = res
        return dp[remain][count][last]

    answer = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        answer.append(dfs(n, k, pn))
    return '\n'.join(map(str, answer))
