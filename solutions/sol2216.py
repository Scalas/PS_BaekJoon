import sys

input = sys.stdin.readline
sys.setrecursionlimit(50000)
INF = 10 ** 9


# 2216 문자열과 점수
# 두 문자열의 사이에 공백을 적절히 끼워넣어 같은 길이의 문자열로 만든 뒤 최대점수를 만드는 문제
# 공백을 끼워넣은 후 두 문자열의 같은 인덱스를 비교하여 두 문자가 같다면 a점을,
# 두 문자중 하나가 공백이라면 b점을, 둘 모두 공백이 아니고 서로 다르다면 c점을 획득
# 단, 두 문자 모두 공백이 될 수는 없다.
def sol2216():
    a, b, c = map(int, input().split())
    x = input().rstrip()
    y = input().rstrip()
    
    # dp[i][j]는 x의 i번째 문자, y의 j번째 문자를 비교할 차례일 때
    # 앞으로 얻을 수 있는 최대점수
    n, m = len(x), len(y)
    dp = [[INF] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][m] = (n - i) * b
    for i in range(m + 1):
        dp[n][i] = (m - i) * b

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            res = max(dp[i + 1][j], dp[i][j + 1]) + b
            if x[i] == y[j]:
                res = max(res, dp[i + 1][j + 1] + a)
            else:
                res = max(res, dp[i + 1][j + 1] + c)
            dp[i][j] = res

    return dp[0][0]
