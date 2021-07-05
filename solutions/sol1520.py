import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


# 1520 내리막길
# 격자형태의 지도에서 인접한 칸 중 현재 칸보다 높이가 낮은 칸으로만 이동 가능할 때
# 좌측 상단에서 우측 하단으로 이동할 수 있는 경우의 수를 모두 구하는 문제
# DFS로 풀 수 있는 간단한 문제지만 동적계획법을 사용하지 않으면 중복계산이 많아 시간초과가 발생한다
# 마지막 칸에 도착할 경우 1을 반환하여 각 칸에서 시작했을 때의 경우의 수를 저장해두고
# 그 칸을 다시 방문하게될 경우 재활용하여 중복연산을 줄일 수 있다
def sol1520():
    m, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]
    dp = [[-1] * n for _ in range(m)]
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def pathsearch(r, c):
        # 도착
        if r == m - 1 and c == n - 1:
            return 1

        # 처음 탐색하는 칸이라면
        if dp[r][c] == -1:
            # 갈 수 있는 방향을 탐색
            res = 0
            for d in direction:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] < board[r][c]:
                    res += pathsearch(nr, nc)
            dp[r][c] = res
        return dp[r][c]

    print(pathsearch(0, 0))
