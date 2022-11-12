import sys

input = sys.stdin.readline


# 4095 최대 정사각형
# 주어진 n * m 격자상에서 1로만 이루어진 정사각형의 최대크기를 구하는 문제
def sol4095():
    answers = []
    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            break
        board = [list(map(int, input().split())) for _ in range(n)]
        dp = [[[0] * 3 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                dp[i][j][:] = [board[i][j]] * 3

        # dp[i][j] 는 (i, j)를 오른쪽 아래로 하는 정사각형의 최대크기(너비)
        # board[i][j] 가 0이라면 0
        # 0이 아니라면 (i - 1, j - 1)에서 끝나는 정사각형과 합쳐서 만들 수 있는 최대 크기를 구하고
        # 만약 합쳐서 정사각형을 만들 수 없다면 1이 된다.
        for i in range(1, n):
            for j in range(1, m):
                if board[i][j] == 0:
                    continue

                dp[i][j][1] += dp[i][j - 1][1]
                dp[i][j][2] += dp[i - 1][j][2]

                if board[i][j] == 0:
                    dp[i][j][0] = 1
                    continue

                dp[i][j][0] = min(dp[i - 1][j - 1][0] + 1, dp[i][j][1], dp[i][j][2])

        answer = 0
        for i in range(n):
            for j in range(m):
                answer = max(answer, dp[i][j][0])

        answers.append(answer)

    return '\n'.join(map(str, answers))
