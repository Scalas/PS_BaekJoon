import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


# 1103 게임
# n * m 격자맵의 각 칸에 숫자가 적혀있고 해당 칸에 서있으면
# 상하좌우로 해당 칸에 쓰여진 숫자만큼 이동 가능하다.
# 이동할 수 있는 칸이 구멍(H)이거나 맵 밖일 경우 게임이 종료된다
# (0, 0)에서 출발하여 이동할 수 있는 최대 횟수를 구하는 문제
def sol1103():
    n, m = map(int, input().split())

    # 구멍을 0으로 치환하여 맵의 상태를 저장
    board = [[int(i) if i.isdigit() else 0 for i in input().rstrip()] for _ in range(n)]

    # dp[i][j] 는 현재 (i, j)칸에 있을 때 이동 가능한 최대 횟수
    dp = [[-1] * m for _ in range(n)]

    # 구멍에서 이동할 수 없기 때문에 구멍에 해당하는 칸은 0으로 초기화
    for i in range(n):
        for j in range(m):
            if not board[i][j]:
                dp[i][j] = 0

    def dfs(r, c):
        # dp[r][c]가 이미 계산되어있다면 반환
        if dp[r][c] >= 0:
            return dp[r][c]

        # 사이클 검출을 위해 현재 탐색중인 상태임을 표시
        dp[r][c] = -2

        cnt = 0

        # 현재칸에 써있는 이동거리
        d = board[r][c]

        # 상하좌우로 이동
        for nr, nc in [(r-d, c), (r+d, c), (r, c-d), (r, c+d)]:
            # 이동가능한 칸일 경우
            if 0 <= nr < n and 0 <= nc < m:
                # 갈 수 있는 위치중 현재 탐색중인 칸이 있다면
                # 사이클이 존재한다는 의미 => 가능한 이동횟수는 무한이므로 -1 반환
                if dp[nr][nc] == -2:
                    return -1

                # 다음 칸에서부터의 최대 이동횟수
                res = dfs(nr, nc)

                # 사이클이 발견될 경우 -1 반환
                if res < 0:
                    return -1

                # 상하좌우중 가능한 이동횟수가 가장 많은 경우를 찾는다
                cnt = max(cnt, res)
        # 구한 다음칸에서의 최대 이동횟수에 다음칸으로 이동한 1회를 추가하여 저장하고 반환
        dp[r][c] = cnt + 1
        return dp[r][c]

    # (0, 0)에서 가능한 최대 이동횟수를 반환
    return dfs(0, 0)
