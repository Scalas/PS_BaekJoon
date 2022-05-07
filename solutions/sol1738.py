import sys

input = sys.stdin.readline
INF = 10 ** 9


# 1738 골목길
# 골목길(간선) m개와 그 교차지점(정점) n개가 주어지고
# 골목길마다 일정 금액을 얻거나 갈취당한다고 할 때,
# 1번교차점에서 n번 교차점으로 가는 경로중 소지금이 최대가 되는 경로를 찾는 문제
# 단, 소지금이 최대가 되는 최적의 경로가 존재하지 않을 경우 -1을 출력
def sol1738():
    n, m = map(int, input().split())

    # 간선 정보저장, 그래프 작성
    g = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        edges.append((u, v, w))

    # a에서 b로 갈 수 있는지 확인하는 함수
    def bfs(a, b):
        visited = [False] * (n + 1)
        q = [a]
        visited[a] = True
        while q:
            nq = []
            for cur in q:
                for nxt, weight in g[cur]:
                    if not visited[nxt]:
                        if nxt == b:
                            return True
                        visited[nxt] = True
                        nq.append(nxt)

            q = nq
        return False

    # 벨만-포드 알고리즘을 사용하여 소지금이 최대가되는 최적경로 구하기
    dp = [-INF] * (n + 1)
    trace = [0] * (n + 1)
    dp[1] = 0
    for _ in range(n-1):
        for u, v, w in edges:
            if dp[u] + w > dp[v]:
                dp[v] = dp[u] + w
                trace[v] = u

    # 만약 n번째에도 갱신이 발생한다면 사이클 발생
    for u, v, w in edges:
        # 사이클이 발생한 곳에서 n번째 교차점으로 갈수있는지 확인
        # 갈 수 있다면 최적의 경로는 존재하지 않음
        if dp[u] + w > dp[v]:
            if bfs(v, n):
                return -1

    # 최적의 경로를 역추적하며 경로 확인, 반환
    answer = []
    cur = n
    while cur:
        answer.append(cur)
        cur = trace[cur]

    return ' '.join(map(str, answer[::-1]))
