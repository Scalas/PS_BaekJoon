import sys

input = sys.stdin.read


# 1958 LCS 3
# 세 문자열의 최장 공통 부분 문자열을 구하는 문제
def sol1958():
    a, b, c = input().split()
    al, bl, cl = len(a), len(b), len(c)

    # dp[i][j][k] 는 문자열 a의 i번째 문자까지, b의 j번째 문자까지, c의 k번째 문자까지 비교했을 때
    # 최장 공통 부분 문자열의 길이
    dp = [[[0] * cl for _ in range(bl)] for _ in range(al)]

    # 세 문자열의 인덱스가 모두 0인 경우 초기화
    dp[0][0][0] = 1 if a[0] == b[0] == c[0] else 0

    # 두 문자열의 인덱스가 0인 경우 초기화
    for i in range(al):
        dp[i][0][0] = 1 if a[i] == b[0] == c[0] else dp[i-1][0][0]

    for i in range(bl):
        dp[0][i][0] = 1 if a[0] == b[i] == c[0] else dp[0][i-1][0]

    for i in range(cl):
        dp[0][0][i] = 1 if a[0] == b[0] == c[i] else dp[0][0][i-1]

    # 한 문자열의 인덱스가 0인 경우 초기화
    for i in range(1, al):
        for j in range(1, bl):
            dp[i][j][0] = 1 if a[i] == b[j] == c[0] else max(dp[i-1][j][0], dp[i][j-1][0])

    for i in range(1, al):
        for j in range(1, cl):
            dp[i][0][j] = 1 if a[i] == b[0] == c[j] else max(dp[i-1][0][j], dp[i][0][j-1])

    for i in range(1, bl):
        for j in range(1, cl):
            dp[0][i][j] = 1 if a[0] == b[i] == c[j] else max(dp[0][i-1][j], dp[0][i][j-1])

    # dp[i][j][k] = dp[i-1][j-1][k-1] if a[i] == b[j] == c[k] else max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    for i in range(1, al):
        for j in range(1, bl):
            for k in range(1, cl):
                if a[i] == b[j] == c[k]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

    # dp[al][bl][cl] (dp[-1][-1][-1]) 반환
    return dp[-1][-1][-1]
