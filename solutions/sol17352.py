import sys

input = sys.stdin.readline


# 17352 여러분의 다리가 되어 드리겠습니다!
# n 개의 노드와 n - 1 개의 간선으로 이루어진 연결그래프에서 1개의 간선을 제거한 그래프가 주어졌을 때
# 간선을 하나 추가하여 다시 그래프를 연결그래프로 만들 수 있는 두 노드의 번호를 구하는 문제
def sol17352():
    n = int(input())
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 2):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    def bfs(start):
        q = [start]
        while q:
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    if visited[nxt]:
                        continue
                    visited[nxt] = True
                    nq.append(nxt)
            q = nq

    # 두 그룹에 속하는 가장 번호가 빠른 노드를 각각 구한다.
    answer = []
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            answer.append(i)
            bfs(i)

    return ' '.join(map(str, answer))
