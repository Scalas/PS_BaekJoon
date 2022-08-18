import sys

input = sys.stdin.readline


# 16947 서울 지하철 2호선
# n개의 역과 n개의 간선으로 이루어진 그래프에서
# 각 정점으로부터 사이클까지의 최단 거리를 구하는 문제
def sol16947():
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    # dfs 로 사이클 구하기
    visited = [-1] * n

    def cycle(cur, path):
        for nxt in g[cur]:
            if len(path) > 1 and nxt == path[-2]:
                continue
            idx = visited[nxt]
            if idx == -1:
                visited[nxt] = visited[path[-1]] + 1
                path.append(nxt)
                cycle(nxt, path)
                path.pop()
            elif idx >= 0:
                for i in range(idx, len(path)):
                    visited[path[i]] = -2

    for i in range(n):
        if len(g[i]) == 1:
            visited[i] = 0
            cycle(i, [i])
            break

    # bfs로 사이클로부터 각 정점으로의 최단거리 구하기
    answer = [0] * n

    q = []
    for i in range(n):
        if len(g[i]) > 2 and visited[i] == -2:
            q.append(i)

    while q:
        nq = []
        for cur in q:
            for nxt in g[cur]:
                if visited[nxt] == -2:
                    continue
                visited[nxt] = -2
                answer[nxt] = answer[cur] + 1
                nq.append(nxt)
        q = nq

    return ' '.join(map(str, answer))
