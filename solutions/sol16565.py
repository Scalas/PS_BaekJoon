import sys

input = sys.stdin.readline
MOD = 10007


# 16565 N포커
# 52개의 트럼프카드에서 n개의 카드를 고를 때
# 같은 숫자 카드를 네 문양 모두 고르는 경우가
# 한번 이상이라도 나타나는 경우의 수를 모두 구하는 문제
def sol16565():
    # 선택해야 할 카드의 수
    n = int(input())

    # 선택할 카드의 수가 4개 미만이면 이길 수 없음
    if n < 4:
        return 0

    dp = [[0] * 53 for _ in range(53)]

    for i in range(53):
        dp[i][0] = dp[i][i] = 1

    for i in range(2, 53):
        for j in range(1, i):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD

    # 선택할 카드의 수가 40개 이상이라면 반드시 이김
    if n >= 40:
        return dp[52][n]

    # 포함 배제의 원리를 사용하여 하나 이상의 포카드를 완성하는 경우들의 합집합을 구함
    answer = 0
    for i in range(1, n // 4 + 1, 2):
        answer = (answer + dp[13][i] * dp[52 - 4 * i][n - 4 * i]) % MOD

    for i in range(2, n // 4 + 1, 2):
        answer = (answer - dp[13][i] * dp[52 - 4 * i][n - 4 * i]) % MOD

    return answer
