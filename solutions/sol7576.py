import sys
from collections import deque

input = sys.stdin.readline
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# 7576 토마토
# bfs로 토마토 익히기 문제
def sol7576():
    m, n = map(int, input().split())
    tomato = [input().split() for _ in range(n)]

    q = deque()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == '1':
                q.append((i, j, 0))
            elif tomato[i][j] == '0':
                cnt += 1

    answer = 0
    while q and cnt:
        r, c, t = q.popleft()
        t += 1
        for d in direction:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < n and 0 <= nc < m and tomato[nr][nc]=='0':
                tomato[nr][nc] = '1'
                cnt -= 1
                answer = t
                q.append((nr, nc, t))

    print(-1 if cnt else answer)
