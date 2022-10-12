import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10 ** 9


# 16928 뱀과 사다리 게임
# 1부터 100까지의 칸으로 이루어진 보드판에
# 각 칸을 이어주는 n개의 사다리(높은 칸으로 가는 루트)와 뱀(낮은 칸으로 가는 루트)가 존재한다.
# 1에서 6 사이의 값을 가지는 주사위를 최소 몇번 굴려야 1부터 100까지 갈 수 있는지 구하는 문제
def sol16928():
    n, m = map(int, input().split())
    g = [[] for _ in range(100)]
    real = [-1] * 100

    # 각 칸을 밟을 시 이동하게 되는 칸을 구함
    for _ in range(n + m):
        u, v = map(lambda x: int(x) - 1, input().split())
        real[u] = v
    
    # 주사위를 한 번 굴려 도착할 수 있는 칸에 대해
    # 각 칸을 밟게될 경우 최종적으로 이동하게 되는 칸을 인접한 칸으로 취급
    for i in range(100):
        for j in range(1, 7):
            nxt = i + j
            if nxt>= 100:
                break
            while real[nxt] != -1:
                nxt = real[nxt]
            g[i].append(nxt)
    
    # bfs 를 수행하여 주사위를 굴려야할 최소 횟수를 구함
    q = [0]
    visited = [False] * 100
    visited[0] = True
    answer = 0
    while q:
        answer += 1
        nq = []
        for cur in q:
            for nxt in g[cur]:
                if visited[nxt]:
                    continue
                if nxt == 99:
                    return answer
                visited[nxt] = True
                nq.append(nxt)
        q = nq

    return -1
