import sys

input = sys.stdin.read


# 10422 괄호
# 괄호로만 이루어져있는 문자열을 괄호 문자열이라 할 때
# 길이가 n이며 괄호 쌍이 올바르게 매칭되는 괄호문자열의 갯수를 구하는 문제
def sol10422():
    _, *case = map(int, input().split())
    n = max(case)
    mod = 1000000007
    dp = [[0, 0, 0] for _ in range(max(n+1, 4))]
    dp[2] = [0, 1, 1]

    # dp[n][0] 은 길이가 n인 괄호문자열중 두개 이상의 독립된 올바른 괄호문자열의 합으로 이루어진 괄호문자열의 갯수
    # dp[n][1] 은 길이가 n인 괄호문자열중 하나의 괄호 안에 올바른 괄호문자열이 들어있는 형태의 괄호문자열의 갯수
    # dp[n][2] 는 dp[n][0] + dp[n][1]
    # dp[n][0] = (dp[2][1] * dp[n-2][2]) + (dp[4][1] * dp[n-4][2]) + ... + (dp[n-2][1] * dp[2][2])
    # dp[n][1] = dp[n-2][2]
    for i in range(4, n+1, 2):
        for j in range(2, i, 2):
            dp[i][0] = (dp[i][0] + dp[j][1] * dp[i-j][2]) % mod
        dp[i][1] = dp[i-2][2]
        dp[i][2] = (dp[i][0] + dp[i][1]) % mod
    return '\n'.join(map(str, [dp[c][2] for c in case]))
