import sys

input = sys.stdin.readline


# 3067 Coins
# n개의 동전의 종류가 주어지고 만들어야할 금액이 주어졌을 때
# 동전으로 금액을 만들 수 있는 경우의 수를 구하는 문제
def sol3067():
    answers = []
    for _ in range(int(input())):
        n = int(input())
        coins = list(map(int, input().split()))
        target = int(input())
        dp = [[0] * n for _ in range(target + 1)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, target + 1):
            for j in range(n):
                coin = coins[j]
                if i - coin >= 0:
                    dp[i][j] = dp[i - coin][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        answers.append(dp[-1][-1])
    return '\n'.join(map(str, answers))
