import sys

input = sys.stdin.readline
INF = 10 ** 9


# 17471 게리맨더링
# n개의 노드로 구성된 그래프가 주어졌을 때
# 그래프를 두개의 연결된 그래프로 나누고 두 그래프의 노드의 값의 차의 최솟값을 구하려고 한다.
# 단, 만약 어떤 노드와 연결되기 위해 다른 그룹에 속한 노드를 거쳐야만 한다면 그 노드와는 연결되어있지 않은 것이다.
def sol17471():
    n = int(input())
    populations = list(map(int, input().split()))
    total = sum(populations)

    g = [[] for _ in range(n)]
    for i in range(n):
        _, *adj = map(lambda x: int(x) - 1, input().split())
        g[i] = adj

    # 그래프를 cur 부터 깊이우선탐색하여 탐색한 노드의 값의 합을 반환
    def dfs(cur, visited):
        visited[cur] = True
        size = populations[cur]
        for nxt in g[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                size += dfs(nxt, visited)
        return size

    # 주어진 cluster의 노드들이 실제로 그 노드들만으로 연결되어있는 그래프인지 확인
    def check_cluster(cluster):
        visited = [True] * n
        for node in cluster:
            visited[node] = False
        dfs(cluster[0], visited)
        for node in cluster:
            if not visited[node]:
                return False
        return True

    # 주어진 클러스터를 제외한 노드들의 집합 또한 클러스터인지 확인하고
    # 맞다면 두 클러스터의 노드의 값의 합의 차를 반환 
    # 나머지가 클러스터가 아니라면 INF 반환
    def search_remain(cluster):
        nonlocal n, total

        visited = [False] * n
        cluster_size = sum(map(lambda x: populations[x], cluster))

        if cluster_size == total:
            return INF

        for node in cluster:
            visited[node] = True

        remain_size = total - cluster_size

        target_node = -1
        for node in cluster:
            for nxt in g[node]:
                if not visited[nxt]:
                    target_node = nxt
                    break
            if target_node != -1:
                break
        remain = dfs(target_node, visited)
        if remain != remain_size:
            return INF
        return abs(cluster_size - remain_size)

    # 두 그래프를 나누는 모든 경우의 수에 대해
    # 정상적으로 나눠진 그래프인지 확인 후
    # 두 그래프의 노드의 값의 합의 차중 최솟값을 구한다.
    first_cluster = []
    answer = INF

    def select(cur):
        nonlocal answer

        if cur == n:
            if not first_cluster:
                return
            if not check_cluster(first_cluster):
                return
            answer = min(answer, search_remain(first_cluster))
            return

        select(cur + 1)

        first_cluster.append(cur)
        select(cur + 1)
        first_cluster.pop()

    select(0)

    return answer if answer != INF else -1
