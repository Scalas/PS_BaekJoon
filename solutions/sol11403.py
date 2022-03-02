import sys

input = sys.stdin.readline


# 11403 경로 찾기
# 가중치없는 방향 그래프 g가 주어졌을 때
# 모든 정점 i, j에 대해 i에서 j로 가는 경로가 있는지 여부를 구하는 문제
# 플로이드-워셜 알고리즘을 응용하여 해결 가능
def sol11403():
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = max(g[i][j], g[i][k]*g[k][j])
    return '\n'.join([' '.join(map(str, line)) for line in g])
