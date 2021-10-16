import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline


# 1922 네트워크 연결
# MST 문제

# Kruskal 알고리즘을 사용한 풀이
def sol1922():
    n = int(input())
    m = int(input())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
    edges.sort()
    answer = 0
    ec = 1
    u = [-1] * (n+1)
    for c, a, b in edges:
        if union(u, a, b):
            answer += c
            ec += 1
            if ec == n:
                break
    return answer


def union(u, x, y):
    x = find(u, x)
    y = find(u, y)
    if x != y:
        if u[x] < u[y]:
            u[x] += u[y]
            u[y] = x
        else:
            u[y] += u[x]
            u[x] = y
        return True
    return False


def find(u, x):
    if u[x] < 0:
        return x
    u[x] = find(u, u[x])
    return u[x]


# Prim 알고리즘을 사용한 풀이
def sol1922_2():
    n = int(input())
    m = int(input())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a].append([c, b])
        g[b].append([c, a])

    q = g[1][::]
    heapify(q)
    answer = 0
    cnt = 1
    visited = [False] * (n+1)
    visited[1] = True
    while q:
        w, v = heappop(q)
        if not visited[v]:
            visited[v] = True
            answer += w
            cnt += 1
            if cnt == n:
                break
            for e in g[v]:
                if not visited[e[1]]:
                    heappush(q, e)
    return answer
