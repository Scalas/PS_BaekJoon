import sys

input = sys.stdin.readline
INF = 100


# 1389 케빈 베이컨의 6단계 법칙
# n명의 사람들간의 연결관계가 주어졌을 때
# 다른 사람과 연결되기 위해 거쳐야할 단계를 모두 합한 값이 가장 작은 사람을 구하는 문제
# 결국 특정 노드에서 다른 노드들로 이동하기 위한 최단거리의 합이 가장 작은 노드를 구하는 문제가 된다.
# n 번의 bfs 를 사용해서 해결할 수도 있지만 플로이드-워셜 알고리즘을 사용하면 더 간단하게 해결할 수 있다.
def sol1389():
    n, m = map(int, input().split())
    g = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        g[i][i] = 0
    for _ in range(m):
        u, v = map(int, input().split())
        g[u][v] = g[v][u] = 1

    for m in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                g[i][j] = min(g[i][j], g[i][m] + g[m][j])
    return min([(sum(g[i]), i) for i in range(1, n + 1)])[1]
