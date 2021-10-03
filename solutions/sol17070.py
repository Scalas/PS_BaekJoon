import sys

input = sys.stdin.readline


# 17070 파이프 옮기기 1
# (1, 1), (1, 2) 의 두 칸을 차지하도록 가로로 놓여진 파이프를 규칙에 따라 이동 및 회전하여
# 한쪽 끝이 (n, n) 에 닿게 하도록 하는 경우의 수를 구하는 문제

# 규칙
# 1. 파이프가 가로로 놓여져있을 경우
#    * 방향은 그대로 오른쪽으로 한칸 이동
#    * 방향을 우하단 대각으로 하고 오른쪽으로 한칸 이동
# 2. 파이프가 세로로 놓여져있을 경우
#    * 방향은 그대로 아래쪽으로 한칸 이동
#    * 방향을 우하단 대각으로 하고 아래쪽으로 한칸 이동
# 3. 파이프가 우하단 대각으로 놓여져있을 경우
#    * 방향은 그대로 우하단 대각으로 한칸 이동
#    * 방향을 가로로 하고 우하단 대각으로 한칸 이동
#    * 방향을 세로로 하고 우하단 대각으로 한칸 이동
def sol17070():
    # 격자판의 크기
    n = int(input())

    # 격자판의 상태 (0은 빈칸, 1은 벽)
    board = [[0, *map(int, input().split())] if _ else [0] * (n + 1) for _ in range(n + 1)]

    # dp[i][j][k] 는 (i, j)에 파이프 한쪽 끝이 닿도록 할 수 있는 경우의 수 중 방향이 k인 경우의 수
    # 0: 가로, 1: 세로, 2: 우하단 대각
    dp = [[[0, 0, 0] for _ in range(n + 1)] for _ in range(n + 1)]

    # 초기 파이프는 (1, 1), (1, 2)를 차지하도록 가로로 놓여있기 때문에 dp[1][2][0] 를 1로 초기화
    dp[1][2][0] = 1

    for i in range(1, n+1):
        for j in range(3, n + 1):
            # 현 위치가 벽일 경우 패스
            if board[i][j]:
                continue

            # dp[i][j]에 가로상태로 도달하기 위해서는 (i, j-1) 칸에서 가로상태 혹은 우하단 대각상태여야 한다
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]

            # dp[i][j] 에 세로상태로 도달하기 위해서는 (i-1, j) 칸에서 세로상태 혹은 우하단 대각상태여야 한다
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]

            # dp[i][j] 에 대각상태로 도달하기 위해서는 (i-1, j-1)칸에서 가로상태, 세로상태, 혹은 우하단 대각상태여야 한다.
            # 단, (i, j-1), (i-1, j) 칸도 벽이 아니어야 한다.
            if not (board[i - 1][j] + board[i][j - 1]):
                dp[i][j][2] = sum(dp[i - 1][j - 1])

    # (n, n)에 도달한 경우의 수를 모두 더하여 반환
    return sum(dp[n][n])
