import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 24444 알고리즘 수업 - 너비 우선 탐색 2
# 그래프를 너비우선탐색했을 때 각 노드의 탐색 순서를 구하는 문제
# 단, 인접 노드는 내림차순으로 방문하며 방문할 수 없는 노드의 순서는 0으로 표현한다.
def sol24445():
    n, m, r = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        heappush(g[u], -v)
        heappush(g[v], -u)

    q = [r - 1]
    answer = [0] * n
    answer[r - 1] = 1
    idx = 2
    while q:
        nq = []
        for cur in q:
            while g[cur]:
                nxt = -heappop(g[cur])
                if not answer[nxt]:
                    answer[nxt] = idx
                    idx += 1
                    nq.append(nxt)
        q = nq

    return '\n'.join(map(str, answer))
