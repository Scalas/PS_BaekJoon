from heapq import heappush, heappop

INF = float('inf')


# 11779 최소비용 구하기 2
# 가중치가있는 그래프에서 최단경로를 구하는 문제
# Dijkstra's Algorithm 을 활용하여 해결 가능
def sol11779(n, m, line, s, e):
    g = [[] for _ in range(n + 1)]
    for a, b, c in line:
        g[a].append((b, c))
    dp = [INF] * (n + 1)
    dp[s] = 0
    path = [-1] * (n + 1)
    q = [(0, s)]
    while q:
        d, cur = heappop(q)
        if d > dp[cur]:
            continue
        for nxt, dist in g[cur]:
            if dp[nxt] > dist + d:
                dp[nxt] = dist + d
                heappush(q, (dp[nxt], nxt))
                path[nxt] = cur
    cost = dp[e]
    res = []
    while e != -1:
        res.append(str(e))
        e = path[e]
    return '\n'.join([str(cost), str(len(res)), ' '.join(res[::-1])])
