import sys

input = sys.stdin.readline


# 14505 팰린드롬 갯수 구하기 (Small)
# 길이 30 이하의 문자열 s가 주어졌을 때 문자열의 부분 문자열(연속하지 않아도 됨) 중
# 팰린드롬인 것의 갯수를 구하는 문제
def sol14505():
    s = input().rstrip()
    n = len(s)

    if n == 1:
        return 1

    # dp[i][j] 는 양 끝 문자가 s[i], s[j] 인 부분 문자열 중 팰린드롬인 것의 갯수
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
        if i < n - 1 and s[i] == s[i + 1]:
            dp[i][i + 1] = 1

    for g in range(3, n + 1):
        for i in range(n - g + 1):
            j = i + g - 1
            if s[i] != s[j]:
                continue
            res = 1
            for u in range(i + 1, j):
                for v in range(u, j):
                    res += dp[u][v]
            dp[i][j] = res

    # 모든 (i, j) 쌍에 대해 양 끝이 s[i], s[j]이고 팰린드롬인 부분 문자열의 갯수를 합하여 반환
    answer = 0
    for i in range(n):
        for j in range(n):
            answer += dp[i][j]
    return answer
