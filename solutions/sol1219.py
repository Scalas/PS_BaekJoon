import sys

input = sys.stdin.readline
INF = float('inf')


# 1219 오민식의 고민
# n개의 도시 0 ~ n-1에 대해
# 도시 사이를 잇는 단방향 노선 m개와 그 노선을 사용하는데 드는 비용,
# 각 도시에 도착시 얻을 수 있는 수익이 주어질 때
# 시작위치 s에서 도착위치 e로 이동했을 때 가지고있을 수 있는 최대 금액을 구하는 문제
# 단, 모든 노선은 몇번이고 이용 가능하며
# 도착이 불가능할 경우에는 gg, 도착시 무한히 많은 돈을 가지고있을 수 있다면 Gee를 출력
def sol1219():
    n, s, e, m = map(int, input().split())

    # 시작지점, 도착지점, 비용으로 구성된 간선리스트를 구성
    edges = []
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, c = map(int, input().split())
        edges.append([u, v, c])
        g[u].append(v)

    # 각 도시에 도착시 얻을 수 있는 수익으로 간선의 비용을 재계산
    profit = list(map(int, input().split()))
    for i in range(len(edges)):
        dst = edges[i][1]
        edges[i][2] -= profit[dst]

    # sp[i] 는 시작지점 s에서 i로 가기 위한 최소비용
    sp = [INF] * n
    sp[s] = 0

    # 탐색 횟수
    cnt = 0
    while cnt < n - 1:
        # 각 간선을 경유하여 최단거리가 갱신되는지 확인
        for u, v, c in edges:
            if sp[u] + c < sp[v]:
                sp[v] = sp[u] + c
        cnt += 1

    # 도착지로 가는 최단거리가 INF일 경우 도달 불가
    if sp[e] == INF:
        return 'gg'

    # 목적지에 도착이 가능할 경우 음수 사이클 체크
    for u, v, c in edges:
        # 추가갱신이 발생할 경우 음수사이클 발견
        if sp[u] + c < sp[v]:
            # 사이클 위치에서 목적지로 갈 수 있는지 확인
            q = [v]
            visited = [False] * n
            visited[v] = True
            while q:
                nq = []
                for cur in q:
                    # 도착 가능하다면 돈을 무한히 가진채로 도착 가능
                    if cur == e:
                        return 'Gee'
                    for nxt in g[cur]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            nq.append(nxt)
                q = nq

    # 그 외의 경우 e에 도달하기 위한 최단거리에 음수값을 취한 뒤
    # 최초에 있던 도시에서 얻은 수익을 합하여 반환
    return profit[s]-sp[e]
