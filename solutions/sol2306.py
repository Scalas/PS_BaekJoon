import sys

input = sys.stdin.readline


# 2306 유전자
# a, t, g, c 네 문자의 반복으로 이루어진 dna 서열이 주어졌을 때
# dna 서열에서 문자를 일부 제거하여 얻을 수 있는 KOI dna 서열의 최대길이를 구하는 문제
# 가장 작은 KOI dna 서열은 at, gc 이며
# X가 KOI 라면 aXt gXc도 KOI 이고
# X와 Y가 KOI 라면 XY도 KOI 이다
def sol2306():
    dna = input().rstrip()
    n = len(dna)

    # dp[i][j] 는 i부터 j까지의 최대 KOI유전자 길이
    dp = [[0] * n for _ in range(n)]

    # KOI 유전자 최대길이
    answer = 0

    # 길이 2인 dna 서열은 at, gc일 경우에 KOI 유전자
    for i in range(n-1):
        u, v = dna[i], dna[i+1]
        if check(u, v):
            dp[i][i+1] = 2

    # 길이를 늘려가며 검사
    for g in range(2, n):
        for i in range(n-g):
            j = i + g

            # 양 끝이 gc 또는 at일 경우 가운데부분의 최대 KOI길이에서 2를 더함
            dp[i][j] = dp[i+1][j-1] + check(dna[i], dna[j])

            # 문자열을 두 부분으로 나누는 경우
            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j])

    # KOI 유전자의 최대 길이 반환
    return dp[0][n-1]


def check(u, v):
    return 2 if (u == 'g' and v == 'c') or (u == 'a' and v == 't') else 0
