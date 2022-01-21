import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float('inf')


# 1162 도로포장
# n개의 도시 사이를 잇는 m개의 도로와 그 도로를 건너는데 걸리는 시간이 주어지고
# 그중 k개 까지의 도로를 포장하여 건너는데 걸리는 시간을 0으로 만들 수 있을 때,
# 1번 도시에서 n번 도시로 가는 최단거리를 구하는 문제
def sol1162():
    n, m, k = map(int, input().split())
    # 도시(노드)와 도로(간선)로 이루어진 그래프
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, d = map(int, input().split())
        g[u-1].append([v-1, d])
        g[v-1].append([u-1, d])

    # dp[i][k] 는 포장 횟수를 k개 남긴채로 i에 도달하는 최단거리
    dp = [[INF] * (k+1) for _ in range(n)]
    for i in range(k+1):
        dp[0][i] = 0

    # 최단거리, 남은 포장횟수, 도시번호
    q = [(0, k, 0)]
    while q:
        d, cnt, mid = heappop(q)
        # d가 mid 까지 포장횟수를 cnt 번 남기고 도달한 최단거리가 아닐 경우
        if dp[mid][cnt] < d:
            continue

        # mid 를 경유하여 갈 수 있는 도시로의 최단거리를 갱신
        for nxt, dst in g[mid]:
            # 도로를 포장하지 않을 경우
            nd = d + dst
            if nd < dp[nxt][cnt]:
                dp[nxt][cnt] = nd
                heappush(q, (nd, cnt, nxt))

            # 도로를 포장할 경우
            if cnt and d < dp[nxt][cnt-1]:
                dp[nxt][cnt-1] = d
                heappush(q, (d, cnt-1, nxt))

    # 마지막 도시에 도달하는 최단거리 반환
    return min(dp[n-1])
