from sys import stdin

input = stdin.readline


# 2293 동전 1
# 동전의 가치의 합이 k가 되도록 하는 경우의 수를 구하는 문제
# 간단한 동적계획법 문제지만 메모리 제한이 4MB인 점에 주의해야한다
def sol2293():
    n, k = map(int, input().split())
    dp = [0] * (k + 1)
    dp[0] = 1
    for coin in stdin:
        coin = int(coin)
        for i in range(k + 1):
            if dp[i] != 0 and i + coin <= k:
                dp[i + coin] += dp[i]
    print(dp[k])
