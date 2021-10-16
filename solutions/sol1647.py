import sys

input = sys.stdin.readline


# 1647 도시 분할 계획
# 마을을 두 개로 분리하고 각 마을안의 집들을 연결하는 길 중에 필요없는 것을 줄여
# 최대한 적은 비용으로 두 마을을 유지하려 할 때, 최소 유지비용을 구하는 문제
# 주어진 도시와 그 사이의 길로 최소 신장 트리를 만들고
# 최소 신장 트리를 구성하는 간선중 가장 가중치가 높은 것을 빼는 것으로 해결
# Kruskal 알고리즘을 사용하여 해결
def sol1647():
    n, m = map(int, input().split())
    edges = [[] for _ in range(1001)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges[c].append([a, b])

    answer = 0
    u = [-1] * (n+1)
    cnt = 1
    for c in range(1001):
        if not edges[c]:
            continue
        for a, b in edges[c]:
            if union(u, a, b):
                cnt += 1
                if cnt == n:
                    break
                answer += c

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