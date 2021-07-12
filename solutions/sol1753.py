import sys
import heapq

input = sys.stdin.readline
INF = float('inf')


# 1753 최단경로
# 주어진 정점에서 시작하여 각 정점으로의 최단거리를 구하는 문제
# 다익스트라 알고리즘을 활용하여 해결 가능하다
def sol1753():
    # 정점의 갯수와 간선의 갯수
    v, e = map(int, input().split())

    # 시작점
    s = int(input())

    # 각 정점의 인접 정점과 그 사이의 거리
    g = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2, d = map(int, input().split())
        g[v1].append((v2, d))

    # 처음에는 모든 정점까지의 거리를 무한으로 초기화(자기 자신과의 거리는 0)
    dp = [INF] * (v + 1)
    dp[s] = 0

    # 경유하는 점의 시작으로 자기 자신을 집어넣음
    # 경유할 수 있는 점 중 가장 거리가 짧은 것을 우선적으로 방문하기 위해 우선순위 큐(heapq)를 사용한다
    q = [(0, s)]
    while q:
        distance, vertex = heapq.heappop(q)
        # 만약 경유할 정점까지의 거리가 최단거리가 아닐 경우 스킵
        if dp[vertex] < distance:
            continue
        # 시작점부터 경유할 정점까지의 거리 + 경유할 정점의 인접 정점까지의 거리로 시작점부터 인접 정점까지의 거리를 갱신
        # 갱신된 경우 해당 정점과 그 정점까지의 거리를 큐에 삽입
        for e, d in g[vertex]:
            c = dp[vertex] + d
            if c < dp[e]:
                dp[e] = c
                # 우선순위 기준을 거리로 잡기 위해 (거리, 정점번호) 의 형태로 큐에 삽입
                heapq.heappush(q, (c, e))
    print('\n'.join(map(conv, dp[1:])))


def conv(num):
    return 'INF' if num == INF else str(num)
