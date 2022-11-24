import sys

input = sys.stdin.readline
INF = 10 ** 9


# 2660 회장뽑기
# n 개의 노드로 이루어진 그래프가 주어졌을 때
# 가장 적은 depth로 너비우선탐색을 마칠 수 있는 시작점을 모두 구하는 문제
def sol2660():
    n = int(input())
    g = [[] for _ in range(n)]
    while True:
        u, v = map(int, input().split())
        if u == v == -1:
            break
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    score, cand = INF, []

    def bfs(start):
        nonlocal score, cand

        visited = [False] * n
        visited[start] = True
        q = [start]
        s = -1
        while q:
            s += 1
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    if visited[nxt]:
                        continue
                    visited[nxt] = True
                    nq.append(nxt)
            q = nq
        if s < score:
            score = s
            cand = [start]
        elif s == score:
            cand.append(start)

    for i in range(n):
        bfs(i)

    return '\n'.join([f'{score} {len(cand)}', f'{" ".join(map(lambda x: str(x + 1), cand))}'])
