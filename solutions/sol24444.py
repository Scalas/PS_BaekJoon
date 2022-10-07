import sys
from heapq import heappush, heappop

input = sys.stdin.readline
sys.setrecursionlimit(500000)


# 24444 알고리즘 수업 - 너비 우선 탐색 1
# 그래프를 너비우선탐색했을 때 각 노드의 탐색 순서를 구하는 문제
# 단, 인접 노드는 오름차순으로 방문하며 방문할 수 없는 노드의 순서는 0으로 표현한다.
def sol24479():
    n, m, r = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        heappush(g[u - 1], (v - 1))
        heappush(g[v - 1], (u - 1))

    answer = [0] * n
    idx = 1
    q = [r - 1]
    answer[r - 1] = idx
    idx += 1

    while q:
        nq = []
        for cur in q:
            while g[cur]:
                nxt = heappop(g[cur])
                if answer[nxt] > 0:
                    continue
                answer[nxt] = idx
                idx += 1
                nq.append(nxt)
        q = nq

    return '\n'.join(map(str, answer))
