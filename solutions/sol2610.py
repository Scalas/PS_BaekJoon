import sys

input = sys.stdin.readline


# 2610 회의준비
# n명의 사람에 대해 m개의 인간관계가 주어졌을 때 서로 아는사이인 사람끼리는
# 하나의 팀이, 그렇지 않은 사람끼린 다른 팀이 되도록 하고
# 각 팀의 팀원들로부터 대표에게로의 의사전달에 거쳐야하는 사람의 수가 가장 적도록 대표를 선출한다.
# 팀의 갯수와 각 팀의 대표가 될 수 있는 사람의 번호를 구하는 문제
def sol2610():
    n = int(input())
    m = int(input())
    g = [[] for _ in range(n+1)]

    # union-find 로 팀을 분할
    u = [-1] * (n+1)
    for _ in range(m):
        v, w = map(int, input().split())
        g[v].append(w)
        g[w].append(v)
        union(u, v, w)

    # rep[i] 는 find의 결과가 i인 사람중 해당 사람을 루트(리더)로 했을 때
    # 트리의 깊이가 가장 낮아지는 사람의 번호
    rep = dict()

    # i번 사람을 루트(리더)로 했을 때 트리의 깊이
    rep_depth = [101] * (n+1)

    # n명의 사람에 대해 깊이 탐색
    for i in range(1, n+1):
        visited = [False] * (n+1)
        q = [i]
        visited[i] = True
        depth = -1
        while q:
            depth += 1
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    if not visited[nxt]:
                        nq.append(nxt)
                        visited[nxt] = True
            q = nq
        rep_depth[i] = depth
        seti = find(u, i)

        # 만약 자신이 속한 팀에서 기존의 리더보다 자신을 리더로 했을 때 깊이가 더 낮다면
        # 자신이 그 팀의 리더가 된다
        if depth < rep_depth[rep.get(seti, 0)]:
            rep[seti] = i
    return '\n'.join([str(len(rep)), *map(str, sorted(rep.values()))])


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
