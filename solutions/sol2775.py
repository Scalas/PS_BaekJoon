import sys

input = sys.stdin.readline
dp = [[0] * 15 for _ in range(15)]
for i in range(15):
    dp[i][1] = 1
    dp[0][i] = i


# 2775 부녀회장이 될테야
# 아파트의 규칙에 따라 k층 n 호에 사는 주민의 수를 구하는 문제
# 아파트의 규칙
# 1. a층 b호에 살기 위해서는 a-1층의 1호부터 b호 까지의 사람을 모두 더한 수 만큼의 사람이 살아야한다
# 2. 0층 i호에는 i명의 사람이 산다


# k층 n호에 사는 사람의 수를 dp[k][n]이라 할때
# dp[k][n]은 dp[k][n-1] + dp[k-1][n] 이 된다
# 이 점화식에 따라 재귀 혹은 반복문으로 풀면 해결 가능하다
def sol2775():
    answer = []
    for t in range(int(input())):
        k, n = [int(input()) for _ in range(2)]
        answer.append(str(count(k, n)))
    print('\n'.join(answer))


def count(k, n):
    global dp
    if (dp[k][n] != 0):
        return dp[k][n]

    if (dp[k][n - 1] == 0):
        dp[k][n - 1] = count(k, n - 1)
    if (dp[k - 1][n] == 0):
        dp[k - 1][n] = count(k - 1, n)
    dp[k][n] = dp[k][n - 1] + dp[k - 1][n]

    return dp[k][n]
