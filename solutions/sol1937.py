import sys

input = sys.stdin.readline


# 1937 욕심쟁이 판다
# 판다는 대나무 숲의 어느 위치에 놓아두면 다음 규칙에 따라 이동한다.
# 1. 현재 위치의 대나무를 모두 먹는다.
# 2. 상, 하, 좌, 우의 위치중 현재 칸보다 대나무 수가 많은 곳으로 이동한다.
# 이때, 판다의 모든 가능한 이동경로의 길이 중 최대길이를 구하는 문제.
def sol1937():
    # 대나무 숲의 크기 (n x n)
    n = int(input())

    # 대나무 숲의 상태
    bamboo = [list(map(int, input().split())) for _ in range(n)]

    # 대나무 숲의 각 위치에서 시작했을 때 최대 이동거리
    dp = [[0] * n for _ in range(n)]

    # 깊이우선탐색 함수
    def dfs(r, c):
        # dp[r][c] 가 계산되지 않았다면
        if not dp[r][c]:
            # 가능한 이동경로중 최장거리를 구한다
            cnt = 0
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < n and 0 <= nc < n and bamboo[nr][nc] > bamboo[r][c]:
                    cnt = max(cnt, dfs(nr, nc))

            # 현재 위치까지 포함하여 dp[r][c] 를 저장
            dp[r][c] = cnt + 1

        # dp[r][c] 반환
        return dp[r][c]

    answer = 0
    # 모든 대나무 숲의 위치에 대해 탐색 수행
    for i in range(n):
        for j in range(n):
            # 아직 탐색하지 않은 위치라면 판다의 시작위치로 잡고 탐색 시작
            if not dp[i][j]:
                dp[i][j] = dfs(i, j)
                # answer 를 갱신
                answer = max(answer, dp[i][j])

    # 판다의 이동경로 최장거리 반환
    return answer
