import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
INF = 10 ** 9


# 12784 인하니카 공화국
# n개의 섬 사이에 다리를 놓아 모든 섬간의 왕래가 가능하게 한 상태에서
# 다리가 하나뿐인 섬으로부터 1번노드로 오는 길을 차단하기 위해 일부 다리를 폭파시켜야하고
# 각 다리를 폭파시키기 위해 필요한 다이너마이트의 갯수가 주어졌을 때
# 필요한 다이너마이트의 최소 갯수를 구하는 문제
def sol12784():
    answers = []
    for _ in range(int(input())):
        # 그래프 구성
        n, m = map(int, input().split())
        g = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v, w = map(int, input().split())
            g[u].append([v, w])
            g[v].append([u, w])

        # 노드 방문 체크
        visited = [False] * (n + 1)

        # 1번 노드부터 탐색 시작
        answer = dfs(g, 1, visited)
        answers.append(answer if answer != INF else 0)
    return '\n'.join(map(str, answers))


# dfs(g, cur, visited) 는 그래프의 구조가 g와 같고
# 현재 노드가 cur 일 때, cur 아래에 있는 모든 리프노드와의 연결을 끊기 위해
# 필요한 다이너마이트의 최소 갯수(노드 cur 아래의 간선만을 끊었을 때의 최솟값)
def dfs(g, cur, visited):
    res = 0
    visited[cur] = True
    for nxt, dc in g[cur]:
        if visited[nxt]:
            continue
        # 자식 노드 아래의 모든 리프노드를 끊는데 드는 비용과
        # 자식노드와의 연결을 끊는데 드는 비용중 최솟값을 취함
        res += min(dc, dfs(g, nxt, visited))

    # 만약 끊어야할 간선이 없다면 자신이 리프노드
    return res if res else INF
