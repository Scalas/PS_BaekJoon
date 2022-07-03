import sys

input = sys.stdin.readline


# 5502 팰린드롬
# 길이 n의 문자열이 주어졌을 때
# 문자열이 팰린드롬 문자열이 되게하기 위해 삽입해야할 문자의 최소 갯수를 구하는 문제
def sol5502():
    n = int(input())
    string = input().rstrip()

    # 문자열의 부분문자열중 팰린드롬인 문자열의 최대길이를 구함
    dp = [[-1] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
        if i < n - 1:
            dp[i][i + 1] = 2 if string[i] == string[i + 1] else 1
    for g in range(2, n):
        for i in range(n - g):
            j = i + g
            dp[i][j] = dp[i + 1][j - 1] + 2 if string[i] == string[j] else max(dp[i + 1][j], dp[i][j - 1])

    # 삽입해야할 문자의 갯수는 (문자열의 전체길이 - 팰린드롬인 최장부분문자열의 길이)
    return n - dp[0][n - 1]
