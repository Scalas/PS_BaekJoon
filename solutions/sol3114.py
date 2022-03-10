import sys

input = sys.stdin.readline


# 3114 사과와 바나나
# n * m 크기의 격자형 땅의 각 칸에 사과나무 혹은 바나나 나무의 갯수가 주어지고
# 불도저가 (0, 0)에서 시작하여 오른쪽, 아래, 오른쪽 아래로만 한칸씩 이동하며
# (n-1, m-1) 에 도착하면 불도저가 지나간 땅을 기준으로 아래 쪽은 A의 땅이, 위 쪽은 B의 땅이 된다고 할 때
# A의 땅의 사과의 갯수와 B의 땅의 바나나의 갯수 합의 최댓값을 구하는 문제
def sol3114():
    n, m = map(int, input().split())

    # a[i][j] 는 (i, j)의 사과의 갯수
    # b[i][j] 는 (i, j)의 바나나의 갯수
    a = [[0] * (m+1) for _ in range(n+1)]
    b = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        line = input().split()
        for j in range(m):
            if line[j][0] == 'A':
                a[i][j] = int(line[j][1:])
            else:
                b[i][j] = int(line[j][1:])

    # a, b의 누적합을 구함
    # a[i][j] 는 (i, 0)부터 (i, j) 까지의 사과의 총 갯수
    # b[i][j] 는 (i, 0)부터 (i, j) 까지의 바나나의 총 갯수
    for i in range(n):
        for j in range(1, m):
            a[i][j] += a[i][j-1]
            b[i][j] += b[i][j-1]

    # dp[i][j] 는 현재 불도저가 (i, j) 번째 칸에 있을 때 지금까지 확정된
    # 위쪽 땅의 사과의 갯수와 아래쪽 땅의 바나나의 갯수의 합의 최댓값
    dp = [[-1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            res = 0

            # 위에서 온 경우
            # (i-1, j) 오른쪽의 땅은 모두 위쪽 땅으로
            # (i, j)의 왼쪽 땅은 모두 아래쪽 땅으로 확정되며
            # 거기에 (i-1, j)까지 확정된 땅들이 더해짐
            if i > 0:
                res = max(res, dp[i-1][j] + b[i-1][m-1] - b[i-1][j] + a[i][j-1])

            # 왼쪽에서 온 경우
            # 추가로 확정되는 땅이 없기 떄문에
            # (i, j-1)까지 확정된 땅을 그대로 가져감
            if j > 0:
                res = max(res, dp[i][j-1])

            # 왼쪽 위에서 온 경우
            # (i-1, j-1) 오른쪽의 땅은 모두 위쪽 땅으로
            # (i, j)의 왼쪽 땅은 모두 아래쪽 땅으로 확정되며
            # 거기에 (i-1, j-1)까지 확정된 땅들이 더해짐
            if i > 0 and j > 0:
                res = max(res, dp[i-1][j-1] + b[i-1][m-1] - b[i-1][j-1] + a[i][j-1])

            dp[i][j] = res

    return dp[n-1][m-1]
