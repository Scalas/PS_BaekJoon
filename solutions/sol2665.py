import sys
from heapq import heappush, heappop

INF = 10 ** 9


# 2665 미로 만들기
# n * n 격자공간에 빈 공간(1)과 벽으로 막힌 공간(0)이 있고
# (0, 0) 에서 (n - 1, n - 1)로 벽을 최대한 적게 없애고 이동하고자 할 때
# 없애야할 벽의 최소 갯수를 구하는 문제
def sol2665():
    n = int(input())
    board = [list(map(lambda x: 1 - int(x), input().rstrip())) for _ in range(n)]
    k = n ** 2

    # 인접한 칸 사이에 간선이 있다고 생각하고 그래프 구성
    # 벽이있는 칸으로의 이동은 1, 없는 칸으로의 이동은 0의 가중치를 가짐
    g = [[] for _ in range(k)]
    for i in range(n):
        for j in range(n):
            cur = n * i + j
            if i > 0:
                g[cur].append((board[i - 1][j], cur - n))
            if i < n - 1:
                g[cur].append((board[i + 1][j], cur + n))
            if j > 0:
                g[cur].append((board[i][j - 1], cur - 1))
            if j < n - 1:
                g[cur].append((board[i][j + 1], cur + 1))

    # (0, 0) 에서 (n - 1, n - 1)로의 최단거리를 구함
    dp = [INF] * k
    q = [(0, 0)]

    while q:
        dest, cur = heappop(q)
        if dp[cur] < dest:
            continue
        for dst, nxt in g[cur]:
            ndst = dest + dst
            if ndst < dp[nxt]:
                dp[nxt] = ndst
                heappush(q, (ndst, nxt))

    return dp[-1]
