import sys
from heapq import heappush, heappop

input = sys.stdin.readline

# 1197 최소 신장 트리
# 그래프가 주어졌을 때 최소신장트리를 구하는 문제


# Kruskal 알고리즘
# 사이클을 만들지 않는 가장 가중치가 적은 간선을 V-1 번 고르는 그리디 알고리즘
# 1. 모든 주어진 간선을 가중치에 따라 오름차순 정렬 - O(ElogE)
# 2. 가중치가 작은 간선부터 시작하여 union-find를 활용하여 간선이 연결하는 두 노드를 union
# 3. union 과정에서 a, b가 이미 mst에 속해있는 경우(사이클이 발생하는 경우) 신장 트리가 아니기 떄문에 제외
# 4. 사이클을 생성하지 않는 간선이라면 정상적으로 union 연산이 실행되고 가중치를 최소신장트리의 비용에 추가
def sol1197():
    v, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(e)]
    edges.sort(key=lambda x: x[2])
    u = [-1] * (v + 1)
    cost = 0
    for a, b, c in edges:
        if union(u, a, b):
            cost += c
    return cost


def union(u, a, b):
    a = find(u, a)
    b = find(u, b)
    if a == b:
        return False
    if u[a] < u[b]:
        u[a] += u[b]
        u[b] = a
    else:
        u[b] += u[a]
        u[a] = b
    return True


def find(u, x):
    if u[x] < 0:
        return x
    u[x] = find(u, u[x])
    return u[x]


# Prim 알고리즘
# mst 의 인접 정점 중 가장 가까이에 있는것을 추가해나가는 알고리즘
# 1. 초기 힙에 (0, 1)을 추가 - 시작점을 1로 잡을 때, mst 와 노드 1과의 거리는 0
# 2. 정점이 추가될 때 마다 그 정점과 연결된 노드 중 아직 mst 에 속해있지 않은 노드와 거리를 heap 에 추가 - O(V)
# 3. heap 에서 꺼낸 노드는 현재 mst 에 인접한 정점 중 가장 가까운 것이 된다.
# 4. mst 로 추가된 정점이 V개가 될 때까지 반복한다 - O(V)
def sol1197_2():
    v, e = map(int, input().split())
    g = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        g[a].append((b, c))
        g[b].append((a, c))

    visit = [False] * (v + 1)
    adj = [(0, 1)]
    cost = 0
    while adj:
        d, node = heappop(adj)
        if not visit[node]:
            visit[node] = True
            cost += d
            for next_node, dst in g[node]:
                if not visit[next_node]:
                    heappush(adj, (dst, next_node))

    return cost


# Kruskal 알고리즘은 O(ElogE),  Prim 알고리즘은 O(N^2) 의 시간복잡도를 가짐
# 노드의 갯수에 비해 간선의 갯수가 매우 많은 경우 Prim 알고리즘이,
# 노드의 갯수가 많은 데 비해 간선의 갯수는 그리 많지 않은 경우 Kruskal 알고리즘의 효율적이다.
