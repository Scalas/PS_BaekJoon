import sys
from collections import deque

input = sys.stdin.readline
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# 2178 미로탐색
# 마지막칸에 가기위한 최단거리 구하기
# 전형적인 bfs 문제
def sol2178():
    n, m = map(int, input().split())
    laby = [input().rstrip() for _ in range(n)]
    turn = [[float('inf')] * m for _ in range(n)]
    q = deque([(0, 0, 1)])
    while q:
        r, c, t = q.popleft()
        if turn[r][c] <= t:
            continue
        turn[r][c] = t
        t += 1
        for d in direction:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < n and 0 <= nc < m and laby[nr][nc] == '1':
                q.append((nr, nc, t))
    print(turn[-1][-1])
