import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float('inf')


# 1956 운동
# 그래프 내에서 가장 짧은 사이클을 찾는 문제
# 시작점의 인접 정점에서 다시 시작점으로 돌아오는 최단거리들의 최솟값을 구하면 해결 가능하다

# 방법 1 Dijkstra's Algorithm
# 모든 정점에 대해 Dijkstra's Algorithm을 사용하여 인접정점으로부터 시작점까지의 최단거리를 구하여
# 그중 최솟값을 취한다
def sol1956():
    v, e = map(int, input().split())
    g = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        g[a].append((b, c))

    answer = INF
    for s in range(1, v + 1):
        dp = [INF] * (v + 1)
        q = []
        for m, d in g[s]:
            dp[m] = d
            heappush(q, (d, m))
        while q:
            dist, vertex = heappop(q)
            if vertex == s:
                answer = min(answer, dist)
                break

            if dist <= dp[vertex]:
                for m, d in g[vertex]:
                    d += dist
                    if d < dp[m]:
                        dp[m] = d
                        heappush(q, (d, m))

    print(-1 if answer == INF else answer)


# 방법 2 Floyd-Warshall Algorithm
# 모든 정점에서 모든 정점으로의 최단거리를 구하는 Floyd-Warshall Algorithm 을 사용하여
# dp[s][m] + dp[m][s] 의 최솟값을 찾는다
# V의 크기가 작아서 충분히 가능한 풀이지만 파이썬에서는 통과하지 못했다
# PyPy3으로는 AC를 받을 수 있다.
def sol1956_2():
    v, e = map(int, input().split())
    dp = [[INF] * (v + 1) for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        dp[a][b] = c

    for m in range(1, v + 1):
        for s in range(1, v + 1):
            for e in range(1, v + 1):
                dp[s][e] = min(dp[s][e], dp[s][m] + dp[m][e])

    answer = INF
    for s in range(1, v + 1):
        answer = min(answer, dp[s][s])
    print(-1 if answer == INF else answer)

