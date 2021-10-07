import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10 ** 9


# 1916 최소 비용 구하기
# n개의 도시에 대해 도시 u 에서 v로 가는 버스노선 m개가 주어졌을 때
# 도시 a 에서 b 로 가는 최소 비용을 구하는 문제
# dijkstra 알고리즘을 사용하여 해결 가능
def sol1916():
    # 노드의 수(도시의 수)
    n = int(input())

    # 간선의 수(버스 노선의 수)
    m = int(input())

    # 그래프 구성
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, c = map(int, input().split())
        g[s].append([e, c])

    # 출발지, 목적지
    a, b = map(int, input().split())

    # 출발지로부터의 거리 리스트
    dp = [INF] * (n + 1)

    # 출발지까지의 거리는 0
    dp[a] = 0

    # (출발지로부터의 거리, 도시번호) 를 원소로 가지는 우선순위 큐
    q = [(0, a)]

    # 출발지로부터 가장 가까운 도시를 경유지로 선택
    while q:
        cost, cur = heappop(q)

        # cur 에 더 적은 비용으로 도달한 경우가 있다면 continue
        if dp[cur] < cost:
            continue

        # cur 을 경유하여 갈 수 있는 모든 도시에 대해 최소비용 갱신
        for nxt, dst in g[cur]:
            d = cost + dst
            # 최소비용이 갱신된 경우 그 도시를 큐에 삽입
            if d < dp[nxt]:
                dp[nxt] = d
                heappush(q, (d, nxt))

    # 목적지까지의 최단거리 반환
    return dp[b]
