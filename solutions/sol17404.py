import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
INF = 10 ** 9


# 17404 RGB 거리 2
# n 개의 집이 직선상에 번호순서대로 있고 각 집을 빨강, 초록, 파랑의 색으로 칠하기 위해 필요한 비용이 주어졌을 때
# 인접한 집 끼리는 색이 같지 않도록 칠하는 경우의 수를 구하는 문제.  단, 1번 집과 n번 집의 색도 서로 달라야한다.
# 완전탐색과 동적계획법을 활용하여 해결할 수 있다.
def sol17404():
    # 집의 갯수
    n = int(input())

    # 각 집을 빨강, 초록, 파랑으로 칠하기 위한 비용
    cost = [list(map(int, input().split())) for _ in range(n)]

    # dp[i][j] 는 i 번째 집의 색이 j 일 때 최소 누적비용
    dp = [[0] * 3 for _ in range(n)]

    # 완전탐색 함수 - 이전집의 색과 현재 집의 번호를 인자로 받는다
    def dfs(pre, cur):
        # 첫 번째 집의 색
        nonlocal f

        # 마지막 집까지 모두 칠했다면 더이상 비용은 들지않는다.
        if cur == n:
            return 0

        # 현재 집을 이전 집과(마지막 집의 경우 첫 번째 집과도) 색이 겹치지 않도록 칠할 때
        # 그 비용을 최소화시킬 수 있는 경우를 구한다
        res = INF
        for c in range(3):
            if (c == pre) or (cur == n - 1 and c == f):
                continue
            if not dp[cur][c]:
                dp[cur][c] = dfs(c, cur + 1) + cost[cur][c]
            res = min(res, dp[cur][c])

        # 현재 집의 색에 따른 총 비용 중 최솟값
        return res

    # 첫 번째 집의 색에 따라 세 번 탐색하여 최소비용을 구함
    answer = INF
    for f in range(3):
        dp = [[0] * 3 for _ in range(n)]
        answer = min(answer, dfs(f, 1) + cost[0][f])

    # 최소비용 반환
    return answer
