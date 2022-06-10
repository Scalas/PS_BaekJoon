import sys

input = sys.stdin.readline


# 16064 Coolest Ski Route
# n개의 노드와 m개의 단방향 간선과 가중치가 주어지고
# 임의의 위치에서 시작하여 더이상 내려갈 수 없을 때 까지 노드를 이동했을 때
# 거친 간선의 가중치의 합의 최댓값을 구하는 문제
# 단, 모든 간선은 내리막길이기 때문에 사이클이 발생할 수 없다.
def sol16064():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]

    # 그래프 파싱 및 진입차수 체크
    degree = [0] * (n + 1)
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append([v, w])
        degree[v] += 1

    # dp[i] 는 i번째 노드에서 멈출 때 까지 지날 수 있는 간선의 가중치의 합의 최댓값
    dp = [0] * (n + 1)

    # 진입 차수가 0인 노드부터 탐색시작
    q = [i for i in range(1, n + 1) if not degree[i]]
    while q:
        nq = []
        for cur in q:
            for nxt, d in g[cur]:
                # 다음 노드의 진입차수 감소
                degree[nxt] -= 1

                # 다음 노드의 dp값을 현재 dp값 + 다음 노드와의 거리로 갱신
                dp[nxt] = max(dp[nxt], dp[cur] + d)

                # 다음 노드의 진입차수가 0이되었다면 큐에 삽입
                if not degree[nxt]:
                    nq.append(nxt)
        q = nq

    return max(dp)
