import sys

input = sys.stdin.readline


# 1976 여행 가자
# 도시간의 연결여부와 방문하고자 하는 도시의 목록이 주어졌을 때
# 방문하려는 도시들을 모두 방문할 수 있는지 알아내는 문제
# 여행계획에 있는 도시들이 모두 직,간접적으로 연결되어있는가, 즉 같은 집합에 속해있는가를 구하면 된다.
# 유니온 파인드를 활용하여 간단하게 해결 가능하다.
def sol1976():
    n = int(input())
    input()
    u = [-1] * (n + 1)
    Map = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if Map[i][j]:
                union(u, i + 1, j + 1)
    f, *plan = map(int, input().split())
    check = find(u, f)
    for p in plan:
        if find(u, p) != check:
            return 'NO'
    return 'YES'


def union(u, a, b):
    a = find(u, a)
    b = find(u, b)
    if a != b:
        if u[a] < u[b]:
            u[a] += u[b]
            u[b] = a
        else:
            u[b] += u[a]
            u[a] = b


def find(u, x):
    if u[x] < 0:
        return x
    u[x] = find(u, u[x])
    return u[x]
