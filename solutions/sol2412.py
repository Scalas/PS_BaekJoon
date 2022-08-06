import sys

input = sys.stdin.readline


# 2412 암벽 등반
# 암벽에 n개의 홈의 좌표가 주어지고 두 좌표의 x좌표의 거리,
# y좌표의 거리가 각각 2를 넘지 않을 때만 서로간에 이동이 가능하다고 할 때
# (0, 0)에서 출발하여 높이가 t인 좌표에 처음으로 도달하기 까지
# 가능한 최소 이동횟수를 구하는 문제
# 단, 만약 높이가 t인 좌표에 도달할 수 없다면 -1을 반환
def sol2412():
    n, t = map(int, input().split())

    # 각 좌표의 노드번호
    pos = {(0, 0): 0}

    # 정상의 좌표 집합
    top = set()

    for i in range(1, n + 1):
        u, v = map(int, input().split())
        pos[(u, v)] = i
        if v == t:
            top.add(i)

    # 모든 좌표들에 대해 이동 가능한 좌표는 x좌표와 y좌표의 거리차이가 각각 2를 넘지 않는 좌표
    # u - 2 ~ u + 2, v - 2 ~ v + 2 이므로 25
    # 상하좌우 2칸 이내의 좌표 25개를 모두 탐색하여 이동 가능한 좌표를 구함
    pos_keys = pos.keys()
    g = [[] for _ in range(n + 1)]
    for u, v in pos_keys:
        cur = pos[(u, v)]
        for i in range(u - 2, u + 3):
            for j in range(v - 2, v + 3):
                # 자기자신은 제외
                if u == i and v == j:
                    continue
                if (i, j) in pos_keys:
                    g[cur].append(pos[(i, j)])

    # 얻은 그래프로 bfs를 사용하여 정상 좌표까지의 최소 이동횟수를 구함
    q = [0]
    visited = [False] * (n + 1)
    visited[0] = True
    answer = 0
    while q:
        answer += 1
        nq = []
        for cur in q:
            for nxt in g[cur]:
                if nxt in top:
                    return answer
                if not visited[nxt]:
                    visited[nxt] = True
                    nq.append(nxt)
        q = nq
    return -1
