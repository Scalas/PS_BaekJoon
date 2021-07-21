import sys
from heapq import heappush, heappop

sys.setrecursionlimit(500000)
input = sys.stdin.readline


# 1167 트리의 지름
# 주어진 트리에서 가장 먼 두 노드간의 거리를 구하는 문제
# DFS 혹은 BFS로 해결가능
def sol1167():
    v = int(input())
    g = [[] for _ in range(v + 1)]
    for _ in range(1, v + 1):
        link = list(map(int, input().split()))
        s = link[0]
        for i in range(1, len(link), 2):
            if link[i] == -1:
                break
            g[s].append((link[i], link[i + 1]))

    visit = [False] * (v + 1)
    answer = -1

    def dfs(n):
        nonlocal answer
        branch = []
        # 각 노드에서 자식노드를 dfs로 탐색
        for c, d in g[n]:
            if not visit[c]:
                visit[c] = True
                heappush(branch, -(dfs(c) + d))

        # 자식노드가 없는 경우 0을 반환
        if not branch:
            return 0

        m = -heappop(branch)

        # 자식노드가 둘 이상일 경우 가장 멀리있는 두 자식노드와의 거리의 합으로 answer를 갱신
        if branch:
            answer = max(answer, m - heappop(branch))

        # 자식노드가 하나이상 있을 경우 가장 멀리있는 자식과의 거리를 반환
        return m

    visit[1] = True
    res = dfs(1)
    return max(res, answer)
