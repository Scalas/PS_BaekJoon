import sys
from math import log2, ceil

input = sys.stdin.readline


# 3176 도로 네트워크
# 트리에서 임의의 두 노드사이의 경로에서 가장 짧은 간선과 가장 긴 간선을 구하는 문제

# LCA 알고리즘을 응용한 풀이
# LCA 알고리즘으로 가장 가까운 공통 조상을 구하되, parent 와는 별도의 sparse table 로
# bs 를 두었다.  bs[u][k] 는 노드 u의 k번째 부모까지의 경로중 가장 짧은 간선과 가장 긴 간선이다.
def sol3176():
    n = int(input())
    k = ceil(log2(n))

    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, d = map(int, input().split())
        g[a].append((b, d))
        g[b].append((a, d))

    depth = [-1] * (n + 1)
    parent = [[0] * k for _ in range(n + 1)]
    bs = [[[0, 0] for __ in range(k)] for _ in range(n + 1)]

    q = [1]
    depth[1] = 0
    while q:
        nq = []
        for cur in q:
            for c, dst in g[cur]:
                if depth[c] < 0:
                    parent[c][0] = cur
                    depth[c] = depth[cur] + 1
                    bs[c][0] = [dst, dst]
                    nq.append(c)
        q = nq

    for j in range(1, k):
        for i in range(1, n + 1):
            parent[i][j] = parent[parent[i][j - 1]][j - 1]
            max_d1, min_d1 = bs[i][j - 1]
            max_d2, min_d2 = bs[parent[i][j - 1]][j - 1]
            bs[i][j] = [max(max_d1, max_d2), min(min_d1, min_d2)]

    answer = []
    for _ in range(int(input())):
        u, v = map(int, input().split())
        max_d, min_d = 0, 10 ** 6

        if depth[u] < depth[v]:
            u, v = v, u

        while depth[u] - depth[v]:
            idx = int(log2(depth[u] - depth[v]))
            b, s = bs[u][idx]
            max_d, min_d = max(max_d, b), min(min_d, s)
            u = parent[u][idx]

        if u != v:
            for j in range(ceil(log2(depth[u])), -1, -1):
                if parent[u][j] != parent[v][j]:
                    b, s = bs[u][j]
                    max_d, min_d = max(max_d, b), min(min_d, s)
                    u = parent[u][j]

                    b, s = bs[v][j]
                    max_d, min_d = max(max_d, b), min(min_d, s)
                    v = parent[v][j]
            b, s = bs[u][0]
            max_d, min_d = max(max_d, b), min(min_d, s)
            b, s = bs[v][0]
            max_d, min_d = max(max_d, b), min(min_d, s)

        answer.append('%d %d' % (min_d, max_d))

    return '\n'.join(answer)
