INF = float('inf')


# 11780 플로이드 2
# 플로이드 알고리즘으로 도시 i에서 j로의 최단거리와 그 경로, 거치게되는 도시의 갯수를 구하는 문제
# 최단거리를 구하는 과정에서 g[s][e] = g[s][m] + g[m][e] 로 갱신할 떄,  pre[s][e]에 m을 대입
# g[s][e]의 경로는 s와 e 사이의 중간점 m,  거기서 다시 s와 m, m과 e 사이의 중간점을 구해나가며 재귀적으로 탐색
def sol11780(n, line):
    g = [[INF] * (n + 1) for _ in range(n + 1)]
    pre = [[-1] * (n + 1) for _ in range(n + 1)]
    # 자신으로의 거리는
    for i in range(1, n + 1):
        g[i][i] = 0

    # a에서 b 까지의 거리 갱신
    # a에서 b로 가는 최단경로 기준 b 이전의 도시 갱신
    for a, b, c in line:
        g[a][b] = min(g[a][b], c)
        pre[a][b] = a

    # 플로이드 알고리즘으로 최단거리를 구함
    for m in range(1, n + 1):
        for s in range(1, n + 1):
            for e in range(1, n + 1):
                if g[s][m] + g[m][e] < g[s][e]:
                    g[s][e] = g[s][m] + g[m][e]
                    # 최단거리가 갱신될 경우 s에서 e로 가는 사이의 경유점은 m
                    pre[s][e] = m

    # 최단거리 테이블을 문자열화
    res = ['\n'.join([' '.join(['0' if i == INF else str(i) for i in line[1:]]) for line in g][1:])]

    # 모든 i, j 쌍에 대해 최단경로가 거치는 도시의 갯수와 경로를 구함
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # i == j 이거나 i에서 j로 가는 경로가 존재하지 않는 경우
            if g[i][j] == 0 or g[i][j] == INF:
                res.append('0')

            # 경로가 존재하는 경우
            else:
                path = trace(pre, i, j)
                res.append(' '.join([str(len(path)), ' '.join(map(str, path))]))
    return '\n'.join(res)


# 경로 추적 함수
def trace(pre, s, e):
    # s에서 e로의 경유지 m
    m = pre[s][e]
    # s에서 e 까지의 최단경로가 s e 인 경우
    if m == s:
        return [s, e]
    # s부터 m, m부터 e까지의 경로를 탐색하여 이어붙임
    # 그대로 이어붙이면 m이 두번 들어가기에 m부터 e 까지의 경로는 첫번째원소를 버림
    return trace(pre, s, m) + trace(pre, m, e)[1:]
