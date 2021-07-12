import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float('inf')


# 9370 미확인 도착지
# 도착지 후보인 c1, c2, ... , ct 중에서 시작점 s에서 출발하여 정점 g, h를 거쳐가는 루트가 최단경로인 경우만을 구하여
# 오름차순 정렬하는 문제

# 1504 특정한 최단경로 문제와 같은 요령으로 g, h를 거친 최단거리를 구한 뒤 s부터의 최단거리와 일치하는지 확인하여
# 리스트에 넣은 뒤 오름차순 정렬하면 해결 가능하다
# 다만 두 최단거리가 모두 INF 인 경우 일치하더라도 불가능한 경로임에 주의
def sol9370():
    answer = []
    for t in range(int(input())):
        n, m, t = map(int, input().split())
        s, g, h = map(int, input().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b, d = map(int, input().split())
            graph[a].append((b, d))
            graph[b].append((a, d))
        cand = [int(input()) for _ in range(t)]

        # 시작점에서의 최단거리
        dp1 = [INF] * (n + 1)
        dp1[s] = 0
        q = [(0, s)]
        while q:
            d, v = heappop(q)
            if dp1[v] < d:
                continue
            for e, dst in graph[v]:
                cost = dp1[v] + dst
                if cost < dp1[e]:
                    dp1[e] = cost
                    heappush(q, (cost, e))

        # g 교차로에서의 최단거리
        dp2 = [INF] * (n + 1)
        dp2[g] = 0
        q = [(0, g)]
        while q:
            d, v = heappop(q)
            if dp2[v] < d:
                continue
            for e, dst in graph[v]:
                cost = dp2[v] + dst
                if cost < dp2[e]:
                    dp2[e] = cost
                    heappush(q, (cost, e))

        # h 교차로에서의 최단거리
        dp3 = [INF] * (n + 1)
        dp3[h] = 0
        q = [(0, h)]
        while q:
            d, v = heappop(q)
            if dp3[v] < d:
                continue
            for e, dst in graph[v]:
                cost = dp3[v] + dst
                if cost < dp3[e]:
                    dp3[e] = cost
                    heappush(q, (cost, e))
        res = []
        # 시작점에서 각 후보지까지의 최단거리와 g, h를 거친 최단거리가 같은 경우
        for c in cand:
            cost = min(dp2[s] + dp2[h] + dp3[c], dp3[s] + dp3[g] + dp2[c])
            if cost != INF and cost == dp1[c]:
                res.append(c)
        res.sort()
        answer.append(' '.join(map(str, res)))
    print('\n'.join(answer))
