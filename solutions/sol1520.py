import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


# 1520 내리막길
# 격자형태의 지도에서 인접한 칸 중 현재 칸보다 높이가 낮은 칸으로만 이동 가능할 때
# 좌측 상단에서 우측 하단으로 이동할 수 있는 경우의 수를 모두 구하는 문제
# DFS로 풀 수 있는 간단한 문제지만 동적계획법을 사용하지 않으면 중복계산이 많아 시간초과가 발생한다
def sol1520():
    # 세로, 가로의 크기
    m, n = map(int, input().split())

    # 각 지점의 높이 데이터
    Map = [list(map(int, input().split())) for _ in range(m)]

    # dp[r][c] 는 Map[0][0] 에서 Map[r][c] 로 이동할 수 있는 경로의 수
    # 방문여부를 나타내기 위해 값은 모두 -1로 초기화
    dp = [[-1] * n for _ in range(m)]

    # 경로 탐색 함수
    def dfs(r, c):
        # 이미 계산된 값이라면 계산해둔 값을 반환
        if dp[r][c] != -1:
            return dp[r][c]

        # 상하좌우 인접칸중  현 지점보다 높은 지점까지의 경로 수를 모두 더한여 dp[r][c]에 저장한다
        dp[r][c] = 0
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= nr < m and 0 <= nc < n and Map[nr][nc] > Map[r][c]:
                dp[r][c] += dfs(nr, nc)

        # 결과값을 반환한다.
        return dp[r][c]

    # 시작지점의 경로 수는 1로 초기화
    dp[0][0] = 1

    # 가장 오른쪽 아래 칸의 경로 수를 탐색하여 결과를 반환
    return dfs(m - 1, n - 1)

