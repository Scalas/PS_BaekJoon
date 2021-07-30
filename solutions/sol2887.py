import sys

input = sys.stdin.readline


# 2887 행성 터널
# 좌표 MST 이지만 거리의 표현이 실제 거리가 아닌 각 x, y, z 좌표끼리의 차의 절댓값중 가장 작은 값이 된다
# 그렇기에 좌표들을 x, y, z 좌표 기준으로 총 세 번 정렬한 뒤 순서상 인접한 점과의 간선만을 취하면
# O(NlogN) 으로 해결 가능하다
# 처음에 문제를 잘못읽고 택시거리로 본 탓에 해결책을 생각하지 못했다
# 문제를 제대로 읽을 것
def sol2887():
    n = int(input())
    planets = []
    for i in range(n):
        x, y, z = map(int, input().split())
        planets.append((x, y, z, i))

    edges = []
    for k in range(3):
        planets.sort(key = lambda x:x[k])
        for i in range(n - 1):
            edges.append((abs(planets[i][k]-planets[i+1][k]), planets[i][3], planets[i+1][3]))

    cnt = 0
    cost = 0
    u = [-1] * n
    edges.sort()
    for d, s, e in edges:
        if union(u, s, e):
            cost += d
            cnt += 1
            if cnt == n-1:
                break
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
