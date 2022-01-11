import sys

input = sys.stdin.readline
INF = 10 ** 9


# 2229 조 짜기
# 학생들을 나이순으로 정렬했을 때 연속한 학생들을 하나의 조로 묶을 수 있다
# 각 조가 잘 짜진 정도가 조에 속한 학생들의 최대점수와 최소점수의 차라고 할 때
# 모든 조의 잘 짜진 정도의 합의 최댓값을 구하는 문제
def sol2229():
    n = int(input())
    score = list(map(int, input().split()))

    # i부터 j까지의 학생으로 조를 짰을 때 잘 짜여진 정도
    degree = [[0] * n for _ in range(n)]
    for i in range(n):
        min_val, max_val = INF, 0
        for j in range(i, n):
            min_val = min(min_val, score[j])
            max_val = max(max_val, score[j])
            degree[i][j] = max_val - min_val

    # dp[i]는 i까지의 학생들로 조를 나누었을 때 잘 짜여진 정도의 합의 최댓값
    # dp[i] = max(degree[0][i], dp[0] + degree[1][i], ... , dp[i-1] + degree[i][i])
    dp = [0] * n
    for i in range(1, n):
        dp[i] = max([dp[j] + degree[j+1][i] for j in range(i)])
        dp[i] = max(dp[i], degree[0][i])

    return dp[-1]
