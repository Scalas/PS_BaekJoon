import sys

input = sys.stdin.readline


# 1890 점프
# N x N 게임판의 각 칸에 수가 적혀있을 때
# 해당 칸에 적힌 수 만큼 아래 또는 오른쪽으로 점프해야한다
# (0, 0) 칸에서 시작하여 (n-1, n-1) 칸에 갈 수 있는 이동 경로의 총 갯수를 구하는 문제
def sol1890():
    # 게임판의 크기
    n = int(input())

    # 게임판의 상태
    board = [list(map(int, input().split())) for _ in range(n)]

    # (0, 0) 칸에서 각 게임판의 칸까지 도달할 수 있는 경로의 갯수
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            # 현재 칸에 적혀있는 수 k
            # 현재 칸까지 도달할 수 있는 경로의 수 cnt
            k, cnt = board[i][j], dp[i][j]

            # 현재 칸이 0(종착점)이 아닐 때
            if k:
                # 아래로 k 만큼 이동한 칸에 현재 칸까지의 이동경로의 갯수를 더한다.
                if i + k < n:
                    dp[i+k][j] += cnt

                # 오른쪽으로 k 만큼 이동한 칸에 현재 칸까지의 이동경로의 갯수를 더한다.
                if j + k < n:
                    dp[i][j+k] += cnt

    # 마지막 칸까지 도달한 이동경로의 갯수 반환
    return dp[-1][-1]
