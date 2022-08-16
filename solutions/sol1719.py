import sys

input = sys.stdin.readline
INF = 10 ** 9


# 1719 택배
# n개의 집하장과 그 사이의 간선, 가중치가 주어졌을 때
# 집하장 i에서 j로 최단 경로로 가기 위해 가장 먼저 이동해야할 다음 집하장을
# 모든 집하장의 쌍 (i, j)에 대해 구하는 문제
def sol1719():
    n, m = map(int, input().split())
    path = [[INF] * n for _ in range(n)]
    answer = [['-'] * n for _ in range(n)]
    for i in range(n):
        path[i][i] = 0

    # 처음에는 직접 연결된 집하장에게로 이동하기 위해 그 집하장으로 먼저 이동해야함
    for _ in range(m):
        u, v, d = map(int, input().split())
        path[u-1][v-1] = path[v-1][u-1] = d
        answer[u-1][v-1] = v
        answer[v-1][u-1] = u

    # 플로이드-워셜 알고리즘을 사용하여 최단거리를 탐색
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if i == k or j == k:
                    continue

                # 최단거리가 갱신될 때마다 다음으로 가야할 집하장을 갱신
                if path[i][k] + path[k][j] < path[i][j]:
                    answer[i][j] = answer[i][k]
                    # 단, k로 직접 갱신하는 것이 아닌 k로 이동하기 위한 다음 집하장으로 갱신해야한다.
                    path[i][j] = path[i][k] + path[k][j]
    return '\n'.join([' '.join(map(str, line)) for line in answer])
