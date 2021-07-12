import sys
import heapq

input = sys.stdin.readline
INF = float('inf')


# 1504 특정한 최단경로
# 최단경로 구하기의 응용문제
# 1번 정점에서 N번 정점까지 임의의 두 정점을 반드시 지나야한다는 조건이 추가
# 1 - v1 - v2 - N 과 1 - v2 - v1 - N 중 더 작은 값을 구하는 문제이기에
# v1, v2에 대해 최단경로 알고리즘을 각각 돌려 해결 가능하다
def sol1504():
    v, e = map(int, input().split())
    g = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2, d = map(int, input().split())
        g[v1].append((v2, d))
        g[v2].append((v1, d))
    m1, m2 = map(int, input().split())

    dp1, dp2 = [INF] * (v + 1), [INF] * (v + 1)
    dp1[m1], dp2[m2] = 0, 0

    q = [(0, m1)]
    while q:
        distance, vertex = heapq.heappop(q)
        if dp1[vertex] < distance:
            continue
        for e, d in g[vertex]:
            c = dp1[vertex] + d
            if c < dp1[e]:
                dp1[e] = c
                heapq.heappush(q, (c, e))
    q = [(0, m2)]
    while q:
        distance, vertex = heapq.heappop(q)
        if dp2[vertex] < distance:
            continue
        for e, d in g[vertex]:
            c = dp2[vertex] + d
            if c < dp2[e]:
                dp2[e] = c
                heapq.heappush(q, (c, e))
    answer = min(dp1[1] + dp1[m2] + dp2[v], dp2[1] + dp2[m1] + dp1[v])
    print(answer if answer != INF else -1)
