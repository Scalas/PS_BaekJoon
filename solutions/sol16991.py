import sys

input = sys.stdin.readline
INF = float('inf')


# 16991 외판원 순회 3
# n 개의 도시를 모두 순회하고 처음 시작한 곳으로 돌아오는 최단 거리를 구하는 문제
def sol16991():
    n = int(input())
    pos = [list(map(int, input().split())) for _ in range(n)]
    m = 2 ** n
    dp = [[-1] * n for _ in range(m)]
    bit = [1 << i for i in range(n)]
    distance = [
        [((pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2) ** 0.5 for j in range(n)] for i in range(n)
    ]

    # 각 도시의 방문상태(비트마스크)와 마지막으로 방문한 위치 last로 메모이제이션
    def dfs(state, last):
        if state == m - 1:
            return distance[last][0]
        if dp[state][last] == -1:
            res = INF
            for nxt in range(n):
                if bit[nxt] & state:
                    continue
                res = min(res, dfs(state | bit[nxt], nxt) + distance[last][nxt])
            dp[state][last] = res
        return dp[state][last]

    return dfs(0, 0)
