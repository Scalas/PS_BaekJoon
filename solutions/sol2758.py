import sys

input = sys.stdin.readline


# 2758 로또
# n과 m이 주어지고 1부터 m까지의 수 중에서 n개의 수를 골라야할 떄
# 가능한 경우의 수를 모두 구하는 문제.
# 단, 매번 마지막에 고른 수의 두 배 이상의 수만을 고를 수 있다.
def sol2758():
    answers = []
    x, y = 10, 2000
    
    # i개의 수를 골랐을 때 j가 마지막 수가 될 경우의 수는
    # j의 절반 이하를 마지막 수로 하여 i - 1개의 수를 고르는 경우의 수의 합
    dp = [[0] * (y + 2) for _ in range(x + 2)]
    for i in range(y + 1):
        dp[0][i] = 1
    for i in range(1, x + 1):
        dp[i][0] = 0
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j // 2]

    for _ in range(int(input())):
        n, m = map(int, input().split())
        answers.append(dp[n][m])

    return '\n'.join(map(str, answers))
