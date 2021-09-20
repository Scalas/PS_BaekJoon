import sys
from math import log2, ceil

input = sys.stdin.readline


# 13511 트리와 쿼리 2
# 트리 상의 두 노드 사이의 경로의 총 비용과 k 번째 정점을 구하는 문제

# sparse table 을 활용한 풀이
def sol13511():
    # 노드의 수
    n = int(input())

    # 노드별 sparse table 의 크기
    k = ceil(log2(n))

    # 그래프 생성
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        g[a].append((b, c))
        g[b].append((a, c))

    # 각 노드의 깊이
    depth = [-1] * (n + 1)

    # parent[i][j] 는 노드 i의 2^j 번째 조상 노드
    parent = [[0] * k for _ in range(n + 1)]

    # cost[i][j] 는 노드 i에서 2^j 번째 조상 노드까지의 비용
    cost = [[0] * k for _ in range(n + 1)]

    # 루트노드 : 1
    depth[1] = 0

    # 루트노드로부터 트리를 탐색
    # 각 노드의 깊이와 부모 노드와 부모 노드까지의 비용을 저장
    q = [1]
    while q:
        nq = []
        for cur in q:
            for c, dst in g[cur]:
                if depth[c] < 0:
                    depth[c] = depth[cur] + 1
                    parent[c][0] = cur
                    cost[c][0] = dst
                    nq.append(c)
        q = nq

    # 조상 노드 리스트와 비용 리스트를 채운다.
    for j in range(1, k):
        for i in range(1, n + 1):
            parent[i][j] = parent[parent[i][j - 1]][j - 1]
            cost[i][j] = cost[i][j - 1] + cost[parent[i][j - 1]][j - 1]

    # 쿼리 처리
    answer = []
    for _ in range(int(input())):
        query = [*map(int, input().split())]
        t, u, v = query[:3]

        # 노드 u가 깊이가 더 큰 쪽의 노드가 되도록 한다.
        if depth[u] < depth[v]:
            u, v = v, u

        # 두 노드의 깊이를 같도록 한다
        while depth[u] - depth[v]:
            u = parent[u][int(log2(depth[u] - depth[v]))]

        # 두 노드의 공통 조상 노드를 탐색
        if u != v:
            for j in range(ceil(log2(depth[u])), -1, -1):
                if parent[u][j] != parent[v][j]:
                    u, v = parent[u][j], parent[v][j]
            u = parent[u][0]

        # 두 노드간의 비용을 계산하는 쿼리인 경우
        if t == 1:
            res = 0
            a, u, v = u, query[1], query[2]

            # 노드 u 로부터 가장 가까운 공통 조상 노드까지의 비용을 모두 합산
            while depth[u] - depth[a]:
                i = int(log2(depth[u] - depth[a]))
                res += cost[u][i]
                u = parent[u][i]

            # 노드 v 로부터 가장 가까운 공통 조상 노드까지의 비용을 모두 합산
            while depth[v] - depth[a]:
                i = int(log2(depth[v] - depth[a]))
                res += cost[v][i]
                v = parent[v][i]

            # 결과 저장
            answer.append(res)

        # 두 노드간의 경로중 k 번째 노드를 구하는 쿼리인 경우
        else:
            a = u
            u, v, i = query[1:]

            # u, v중 어느쪽 노드를 어느 깊이까지 타고 올라가야하는지 구한다.
            if i <= depth[u] - depth[a]:
                d = depth[u] - i + 1
                s = u
            else:
                i -= (depth[u] - depth[a])
                d = depth[a] + i - 1
                s = v

            # 시작노드로부터 필요한 깊이까지 타고 올라간다.
            while depth[s] - d:
                s = parent[s][int(log2(depth[s] - d))]

            # 결과 저장
            answer.append(s)

    # 출력 형식에 맞춰 결과 리스트 반환
    return '\n'.join(map(str, answer))
