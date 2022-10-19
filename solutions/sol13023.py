import sys

input = sys.stdin.readline


# 13023 ABCDE
# 주어진 친구관계 그래프에 A - B - C - D - E 와 같이 5명이
# 연쇄적으로 친구관계인 존재하는지 여부를 구하는 문제
def sol13023():
    n, m = map(int, input().split())

    # 친구관계 그래프
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    # 백트래킹으로 중복노드 없이 깊이 5까지 들어갈 수 있는 시작 노드가 존재한다면
    # 5연쇄 친구 관계가 존재함
    def dfs(cur, depth):
        if depth == 5:
            return True
        for nxt in g[cur]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            if dfs(nxt, depth + 1):
                return True
            visited[nxt] = False
        return False

    visited = [False] * n

    for s in range(n):
        visited[s] = True
        if dfs(s, 1):
            return 1
        visited[s] = False
    return 0
