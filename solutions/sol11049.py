import sys

MAX_VAL = float('inf')


# 11049 행렬 곱셈 순서
# 행과열이 각각 (n, k), (k, m)의 두 행렬을 곱하는데 필요한 곱하기 연산의 수가 n*k*m 일때
# 주어진 모든 행렬을 곱하는데 필요한 곱셈연산의 수의 최솟값을 구하는 문제
# 파일 합치기 문제와 거의 유사한 방식의 동적계획법으로 풀 수 있다
def sol11049():
    n = int(sys.stdin.readline())
    mat = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        dp[i][i + 1] = mat[i][0] * mat[i][1] * mat[i + 1][1]
    for g in range(2, n):
        for i in range(n - g):
            j = i + g
            res = MAX_VAL
            for m in range(i, j):
                res = min(res, dp[i][m] + dp[m + 1][j] + mat[i][0] * mat[m][1] * mat[j][1])
            dp[i][j] = res

    print(dp[0][n - 1])
