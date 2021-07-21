import sys
from heapq import heappush, heappop

sys.setrecursionlimit(500000)
input = sys.stdin.readline


# 1967 트리의 지름
# 1167 문제와 거의 차이가 없는 문제
# 마찬가지로 dfs 혹은 bfs로 해결가능
def sol1967():
    v = int(input())
    g = [[] for _ in range(v + 1)]
    for _ in range(v-1):
        p, c, d = map(int, input().split())
        g[p].append((c, d))

    visit = [False] * (v + 1)
    answer = -1

    def dfs(n):
        nonlocal answer
        branch = []
        for c, d in g[n]:
            if not visit[c]:
                visit[c] = True
                heappush(branch, -(dfs(c) + d))

        if not branch:
            return 0
        m = -heappop(branch)
        if branch:
            answer = max(answer, m - heappop(branch))
        return m

    visit[1] = True
    res = dfs(1)
    return max(res, answer)
