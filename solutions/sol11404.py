import sys

input = sys.stdin.readline
INF = float('inf')


# 11404 플로이드
# 한 정점에서의 최단거리가 아닌 모든 정점에서 모든 정점으로의 최단거리를 구하는 문제
# 플로이드 워셜 알고리즘을 사용하여 해결 가능하다
def sol11404():
    n, m = int(input()), int(input())
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        dist[a - 1][b - 1] = min(dist[a-1][b-1], c)

    for k in range(n):
        for s in range(n):
            for e in range(n):
                dist[s][e] = min(dist[s][e], dist[s][k]+dist[k][e])
    print('\n'.join([' '.join(['0' if d == INF else str(d) for d in line]) for line in dist]))

