import sys
from heapq import heapify, heappop
from itertools import combinations

input = sys.stdin.readline


# 1774 우주신과의 교감
# 이미 연결된 간선이 존재하는 좌표상에서의 MST 문제
# 이미 연결된 정점들에 대해 union 연산을 실행해둔 채로 Kruskal 알고리즘을 사용하여 해결
def sol1774():
    n, m = map(int, input().split())
    gods = [tuple(map(int, input().split())) for _ in range(n)]
    u = [-1] * n
    cnt = 0
    for _ in range(m):
        s, e = map(int, input().split())
        if union(u, s - 1, e - 1):
            cnt += 1
    edges = [(((gods[x][0] - gods[y][0]) ** 2 + (gods[x][1] - gods[y][1]) ** 2) ** .5, x, y) for x, y in
             combinations(range(n), 2)]
    heapify(edges)
    cost = 0
    while cnt < n - 1:
        d, s, e = heappop(edges)
        if union(u, s, e):
            cost += d
            cnt += 1

    return '%.2f' % cost


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
