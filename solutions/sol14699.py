import sys

input = sys.stdin.readline
sys.setrecursionlimit(500000)


# 14699 관악산 등산
# n개의 노드와 그 높이, 노드 사이의 간선이 주어지고
# 각 노드에서 더 높은 노드로만 이동 가능하다고 할 때
# 각 노드에서 출발하여 방문할 수 있는 노드 수의 최댓값을 구하는 문제
def sol14699():
    n, m = map(int, input().split())

    # 높이가 보다 높은쪽을 향해서만 간선을 연결
    heights = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        if heights[u - 1] > heights[v - 1]:
            u, v = v, u
        g[u - 1].append(v - 1)

    # dp[i] 는 i번 노드에서 시작하여 방문 가능한 노드 수의 최댓값
    dp = [-1] * n

    # dfs로 현재 노드에서 방문 가능한 최대 깊이를 탐색
    def dfs(cur):
        if dp[cur] < 0:
            res = 1
            for nxt in g[cur]:
                res = max(res, dfs(nxt) + 1)
            dp[cur] = res
        return dp[cur]

    return '\n'.join(map(str, [dfs(i) for i in range(n)]))
