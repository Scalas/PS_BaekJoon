import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 4386 별자리 만들기
# 2차원 좌표상의 점들이 주어졌을 때 최소신장트리의 비용을 구하는 문제
# 점과 점 사이에 모두 간선이 있는것으로 가정하고 Kruskal 알고리즘을 사용하여 해결
def sol4386():
    n = int(input())
    stars = [tuple(map(float, input().split())) for _ in range(n)]
    edges = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d = ((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** .5
            heappush(edges, (d, i, j))
    u = [-1] * n
    cnt = 0
    cost = 0
    while cnt < n - 1:
        d, i, j = heappop(edges)
        if union(u, i, j):
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
