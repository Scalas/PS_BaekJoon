import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 2211 네트워크 복구
# n개의 노드와 m개의 간선이 주어졌을 때
# 1번노드로부터 다른 노드로의 최단거리를 유지하며 간선의 수를 최소화하는 문제
def sol2211():
    n, m = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append([v, w])
        g[v].append([u, w])

    # 다익스트라 알고리즘으로 슈퍼컴퓨터(1)로부터의 최단거리와 최단경로를 구함
    shortest_dst = [10001] * (n+1)
    shortest_dst[1] = 0
    shortest_path = [-1] * (n+1)
    shortest_path[1] = 0
    q = [(0, 1)]
    while q:
        dst, cur = heappop(q)
        if dst > shortest_dst[cur]:
            continue

        for nxt, nxt_dst in g[cur]:
            distance = dst + nxt_dst
            if distance < shortest_dst[nxt]:
                shortest_dst[nxt] = distance
                shortest_path[nxt] = cur
                heappush(q, (distance, nxt))

    # 각 노드로의 최단경로에 필요한 간선만을 삽입
    answer_edges = []
    for i in range(2, n+1):
        answer_edges.append(' '.join(map(str, [shortest_path[i], i])))

    return '\n'.join([str(len(answer_edges)), '\n'.join(answer_edges)])
