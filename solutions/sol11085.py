import sys

input = sys.stdin.readline


# 11085 군사 이동
# p개의 정점과 w개의 간선, 시작점 c와 도착점 v가 주어지고
# 둘 사이를 잇는 간선중 가중치가 가장 작은 값이 최대가 되도록 경로를 짤 때
# 경로에 속한 간선중 가중치가 가장 작은 값을 구하는 문제
def sol11085():
    p, w = map(int, input().split())
    c, v = map(int, input().split())
    u = [-1] * p

    # 모든 간선을 가중치순으로 내림차순 정렬
    path = [list(map(int, input().split())) for _ in range(w)]
    path.sort(key=lambda x: -x[2])

    # 가장 가중치가 큰 간선부터 이어나가다가
    # 처음으로 시작점과 도착점이 이어진 순간의 간선의 가중치가
    # 경로에 속한 가중치가 가장 작은 간선중 최댓값이 된다.
    for x, y, z in path:
        union(u, x, y)
        if find(u, c) == find(u, v):
            return z

    return 0


# union / find 함수
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


def find(u, x):
    if u[x] < 0:
        return x
    u[x] = find(u, u[x])
    return u[x]
