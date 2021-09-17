import sys
import math

input = sys.stdin.readline


# 11438 LCA 2
# 가장 가까운 공통 조상 구하기 문제
# 노드의 수가 최대 100000이며 질의의 수도 최대 100000이기에
# 매번 조상노드 리스트를 구하는 방식으로 풀면 O(NM)의 시간 복잡도를 보이게 되어 시간초과가 발생한다.

# sparse table(희소 테이블)을 활용하여 문제를 더 효율적으로 해결할 수 있다. 절차는 다음과 같다.
# 1. 각 노드의 깊이를 나타낼 depth 리스트와 부모노드를 나타낼 parent 리스트를 생성한다
#    이 때, parent 리스트는 2차원 리스트이며 parent[i][k] 는 노드 i의 2^k 번 거슬러올라간 조상노드를 의미한다.
#
# 2. dfs 혹은 bfs 로 트리를 순회하며 각 노드의 1번 거슬러올라간 조상노드(parent[i][0])와 깊이를 구한다.
#    이 때, 점화식 parent[i][j] = parent[parent[i][j-1]][j-1] 를 사용해서 O(NK) 의 시간 복잡도로 작업을 수행한다.
#    K는 log(2, N) 을 올림한 값과 같다.
#
# 3. 각 질의(LCA 를 구할 두 노드 u, v) 에 대해 두 노드의 깊이가 같아질 때 까지
#    보다 깊이가 큰 노드를 끌어올린다.
#
# 4. 두 노드가 서로 같다면 그대로 어느 한쪽 노드를 출력
#
# 5. 그렇지 않다면 두 노드의 가장 먼 공통 조상으로부터 처음으로 두 노드의 조상 노드가 달라질 때 까지 탐색
#    탐색 종료 후 노드 u 또는 v의 부모노드를 출력
def sol11438():
    # 각 노드의 깊이와 첫 번째 부모를 구하기 위한 탐색 함수
    def bfs(root):
        q = [root]
        while q:
            nq = []
            for cur in q:
                for c in g[cur]:
                    if depth[c] < 0:
                        depth[c] = depth[cur] + 1
                        parent[c][0] = cur
                        nq.append(c)
            q = nq

    # 노드의 수
    n = int(input())

    # sparse table 의 크기
    k = math.ceil(math.log2(n))

    # 그래프 생성
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    # 각 노드의 깊이 리스트
    depth = [-1] * (n + 1)

    # 각 노드의 조상 노드 리스트 (sparse table)
    parent = [[-1] * k for _ in range(n + 1)]

    # 루트 노드인 1의 깊이를 0으로 하고 탐색 시작
    depth[1] = 0
    bfs(1)

    # sparse table 채우기
    for j in range(1, k):
        for i in range(1, n + 1):
            parent[i][j] = parent[parent[i][j - 1]][j - 1]

    # 각 질의에 대해 정답 구하기
    answer = []
    for _ in range(int(input())):
        u, v = map(int, input().split())

        # 노드 u가 노드 v 보다 깊이가 크도록 한다
        if depth[u] < depth[v]:
            u, v = v, u

        # 두 노드의 깊이가 같아질 때 까지 노드 u를 끌어올린다
        while depth[u] - depth[v]:
            u = parent[u][int(math.log2(depth[u] - depth[v]))]

        # 두 노드가 같지 않다면
        if u != v:
            # 가장 먼 공통 조상 노드로부터 처음으로 두 노드의 조상 노드가 달라질 때 까지 탐색
            for j in range(math.ceil(math.log2(depth[u])), -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]

            # 현재 u와 v는 공통 조상노드의 자식 노드인 상태이므로 둘 중 하나는 부모노드를 방문
            u = parent[u][0]

        # 노드 u 혹은 v를 반환
        answer.append(u)

    # 출력 형식에 맞춰 정답리스트 반환
    return '\n'.join(map(str, answer))
