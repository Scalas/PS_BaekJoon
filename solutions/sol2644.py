import sys

input = sys.stdin.readline


# 2644 촌수계산
# 트리형태로 주어진 족보를 토대로 두 사람의 촌수를 계산하는 문제
# 트리상에서 두 노드 사이의 거리를 구하는 문제와 같다.
def sol2644():
    n = int(input())
    u, v = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(int(input())):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)

    visited = [False] * (n+1)
    q = [u]
    visited[u] = True
    chon = 0
    find = False

    while q:
        nq = []
        for cur in q:
            if cur == v:
                find = True
                break
            for child in g[cur]:
                if not visited[child]:
                    visited[child] = True
                    nq.append(child)
        if find:
            break
        q = nq
        chon += 1
    return chon if find else -1
