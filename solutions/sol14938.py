import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10 ** 9


# 14938 서강 그라운드
# n개의 노드가 주어지고 노드중 하나를 선택하여 시작지점으로 한 뒤 그 노드의 아이템을 얻고
# 다른 노드들로의 거리가 m 이하일 경우에만 그 노드의 아이템을 얻을 수 있다.
# 최적의 시작지점을 골랐을 때 얻을 수 있는 최대 아이템 갯수를 구하는 문제
def sol14938():
    n, m, r = map(int, input().split())
    item_count = list(map(int, input().split()))
    g = [[] for _ in range(n)]

    for _ in range(r):
        u, v, d = map(int, input().split())
        g[u - 1].append((d, v - 1))
        g[v - 1].append((d, u - 1))
    
    # 각 시작지점에서 모든 노드로의 최단거리를 구한 뒤
    # 최단거리가 m 이하일 떄만 아이템을 얻은것으로 처리하여
    # 얻을 수 있는 최대 아이템 갯수를 반환
    def simulate(start):
        dp = [INF] * n
        dp[start] = 0
        q = [(0, start)]
        while q:
            dst, cur = heappop(q)
            for dist, nxt in g[cur]:
                ndst = dst + dist
                if ndst >= dp[nxt]:
                    continue
                dp[nxt] = ndst
                heappush(q, (ndst, nxt))
        res = 0
        for i in range(n):
            if dp[i] <= m:
                res += item_count[i]

        return res

    return max([simulate(i) for i in range(n)])
