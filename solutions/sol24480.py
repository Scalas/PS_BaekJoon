import sys
from heapq import heappop, heappush

input = sys.stdin.readline
sys.setrecursionlimit(500000)


# 24480 알고리즘 수업 - 깊이 우선 탐색 2
# 그래프와 시작 노드가 주어지고 시작 노드의 방문 순서가 1일 때
# 깊이우선 순위로 그래프 순회시 나머지 노드의 방문 순서를 구하는 문제
# 단, 인접 노드는 노드 번호 내림차순으로 방문하며, 방문할 수 없는 노드는 0 으로 표시한다.
def sol24480():
    n, m, r = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        heappush(g[u], -v)
        heappush(g[v], -u)

    idx = 1
    answer = [0] * n

    def dfs(cur):
        nonlocal idx

        answer[cur] = idx
        idx += 1

        while g[cur]:
            nxt = -heappop(g[cur])
            if answer[nxt]:
                continue
            dfs(nxt)

    dfs(r - 1)
    return '\n'.join(map(str, answer))
