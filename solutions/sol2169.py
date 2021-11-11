import sys

input = sys.stdin.readline
INF = - 10**9


# 2169 로봇 조종하기
# 왼쪽, 오른쪽, 아래로만 이동 가능한 로봇이 (0, 0) 위치에서 시작하여
# (n-1, m-1)위치로 가는동안 거쳐간 칸의 값의 합의 최댓값을 구하는 문제
def sol2169():
    # 맵의 크기
    n, m = map(int, input().split())

    # 각 칸의 값
    board = [[0, *map(int, input().split())] for _ in range(n)]

    # dp[i][j] 는 (i, j)부터 (n-1, m-1) 까지 거쳐간 칸의 합의 최댓값
    dp = [[INF] * m for _ in range(n)]

    # 마지막 행은 (n-1, m-1)로 가기위해 오른쪽으로 가야함
    dp[-1][-1] = board[-1][-1]
    for i in range(m-2, -1, -1):
        dp[-1][i] = board[-1][i+1] + dp[-1][i+1]

    # 마지막에서 두 번째 열부터 올라오면서 최댓값 갱신
    for i in range(n-2, -1, -1):
        # 왼쪽에서부터 시작하여 왼쪽으로 갈 경우 최댓값과 아래쪽으로 갈 경우 최댓값중
        # 큰 쪽에 현재 칸의 값을 더한 값을 구한다
        tmp = [INF] * m
        tmp[0] = dp[i+1][0] + board[i][1]
        for j in range(1, m):
            tmp[j] = max(tmp[j-1], dp[i+1][j]) + board[i][j+1]

        # 구한 값들로 dp[i]를 갱신
        for j in range(m):
            dp[i][j] = max(dp[i][j], tmp[j])

        # 오른쪽에서부터 시작하여 오른쪽으로 갈 경우 최댓값과 아래쪽으로 갈 경우 최댓값중
        # 큰 쪽에 현재 칸의 값을 더한 값을 구한다
        tmp = [INF] * m
        tmp[m-1] = dp[i+1][m-1] + board[i][m]
        for j in range(m-2, -1, -1):
            tmp[j] = max(tmp[j+1], dp[i+1][j]) + board[i][j+1]

        # 구한 값들로 dp[i]를 갱신
        for j in range(m):
            dp[i][j] = max(dp[i][j], tmp[j])

    return dp[0][0]

