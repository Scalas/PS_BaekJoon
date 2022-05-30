import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10 ** 9


# 2307 도로검문
# n개의 지점과 m개의 도로의 정보가 주어지고 용의자가 1번지점에서 n번지점으로 최단거리로 빠져나가려 할 때
# 경찰이 m개의 도로중 하나를 봉쇄하여 지연시킬 수 있는 용의자의 도주 시간의 최댓값을 구하는 문제
# 만약 무한정 지연시킬 수 있다면 -1을 반환
def sol2307():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u, v, d = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
        distance[u][v] = distance[v][u] = d

    # 다익스트라 최단거리 함수
    def dijkstra(short):
        dp = [INF] * (n + 1)
        q = [(0, 1)]
        dp[1] = 0
        while q:
            if dp[n] <= short:
                return -1

            dst, cur = heappop(q)
            if dst > dp[cur]:
                continue

            for nxt in g[cur]:
                ndst = dst + distance[cur][nxt]
                if ndst < dp[nxt]:
                    dp[nxt] = ndst
                    heappush(q, (ndst, nxt))
        return dp[n]

    # 기존 최단경로를 구하기 위한 다익스트라
    trace = [0] * (n + 1)
    dp = [INF] * (n + 1)
    q = [(0, 1)]
    dp[1] = 0
    while q:
        dst, cur = heappop(q)
        if dst > dp[cur]:
            continue

        for nxt in g[cur]:
            ndst = dst + distance[cur][nxt]
            if ndst < dp[nxt]:
                dp[nxt] = ndst
                trace[nxt] = cur
                heappush(q, (ndst, nxt))

    # 최단 경로를 구성하는 도로만을 추려냄
    edges = []
    cur = n
    while trace[cur]:
        edges.append((cur, trace[cur]))
        cur = trace[cur]

    # 최단 경로를 구성하는 도로를 하나씩 봉쇄해가며 가장
    delayed = dp[n]
    for u, v in edges:
        d = distance[u][v]
        distance[u][v] = distance[v][u] = INF
        delayed = max(delayed, dijkstra(delayed))
        distance[u][v] = distance[v][u] = d
        if delayed == INF:
            return -1

    return delayed - dp[n]
