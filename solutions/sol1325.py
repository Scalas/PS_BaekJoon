import sys

input = sys.stdin.readline


# 1325 효율적인 해킹
# n개의 노드와 m개의 단방향 간선이 주어질 때
# 도달할 수 있는 다른 노드의 갯수가 가장 많은 노드들의 번호를 오름차순으로 구하는 문제
# bfs, dfs를 사용한 브루트포스 / 강한연결요소

# 풀이1 bfs를 사용한 풀이
def sol1325():
    n, m = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[v].append(u)

    cnt = [1] * (n+1)
    cnt[0] = 0

    def bfs(start):
        q = [start]
        visited = [False] * (n+1)
        visited[start] = True
        while q:
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        cnt[start] += 1
                        nq.append(nxt)
            q = nq

    for i in range(1, n+1):
        bfs(i)

    max_cnt = max(cnt)
    pc = [i for i in range(1, n+1) if cnt[i] == max_cnt]
    pc.sort()

    return ' '.join(map(str, pc))
