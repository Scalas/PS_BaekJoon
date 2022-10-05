import sys
from heapq import heappush, heappop

input = sys.stdin.readline
sys.setrecursionlimit(500000)


# 24479 알고리즘 수업 - 깊이 우선 탐색 1
# 양방향 간선으로 이어진 그래프가 주어졌을 때
# 시작노드 R에서 깊이 우선 탐색을 했을 때 각 노드의 방문 순서를 구하는 문제
# 단, 시작 노드의 방문 순서는 1이며 인접 노드는 노드 번호 오름차순으로 방문하고
# 방문할 수 없는 노드의 방문 순서는 0으로 출력한다.
def sol24479():
    n, m, r = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        heappush(g[u - 1], (v - 1))
        heappush(g[v - 1], (u - 1))

    answer = [0] * n
    visited = [False] * n
    visited[r - 1] = True
    idx = 1

    def dfs(cur):
        nonlocal idx
        answer[cur] = idx
        idx += 1
        while g[cur]:
            nxt = heappop(g[cur])
            if not visited[nxt]:
                visited[nxt] = True
                dfs(nxt)
    dfs(r - 1)

    return '\n'.join(map(str, answer))
