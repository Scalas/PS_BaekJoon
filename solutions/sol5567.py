import sys

input = sys.stdin.readline


# 5567 결혼식
# 그래프상에서 노드1과의 거리가 2 이하인 노드의 갯수를 구하는 문제
def sol5567():
    n = int(input())
    g = [[] for _ in range(n+1)]
    for _ in range(int(input())):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    f = []
    invited = [False] * (n+1)
    invited[1] = True
    for nxt in g[1]:
        if not invited[nxt]:
            invited[nxt] = True
            f.append(nxt)

    fof = []
    for friend in f:
        for nxt in g[friend]:
            if not invited[nxt]:
                invited[nxt] = True
                fof.append(nxt)
    return len(f) + len(fof)
