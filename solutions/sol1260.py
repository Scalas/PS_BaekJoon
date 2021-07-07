import sys
from collections import deque

input = sys.stdin.readline


# 1260 DFS와 BFS
# 주어진 그래프를 주어진 정점에서 시작하여 DFS와 BFS로 각각 순회하여 그 순서를 출력
def sol1260():
    n, m, v = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for v1, v2 in [map(int, input().split()) for _ in range(m)]:
        g[v1].append(v2)
        g[v2].append(v1)

    for edge in g:
        edge.sort()

    print(' '.join(map(str, dfs(g, v, [], [0] * (n + 1)))))
    print(' '.join(map(str, bfs(g, v))))


def dfs(g, v, path, visit):
    visit[v] = 1
    path.append(v)
    for nv in g[v]:
        if visit[nv] == 0:
            dfs(g, nv, path, visit)

    return path


def bfs(g, v):
    visit = [0] * len(g)
    path = []
    q = deque([v])

    while q:
        cv = q.popleft()
        if visit[cv] == 1:
            continue
        visit[cv] = 1
        path.append(cv)
        for nv in g[cv]:
            if visit[nv] == 0:
                q.append(nv)
    return path
