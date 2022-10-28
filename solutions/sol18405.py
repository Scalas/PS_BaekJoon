import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 18405 경쟁적 전염
# n * n 격자 공간에 1 ~ k 의 번호를 가진 바이러스가 있고
# 각 바이러스는 1초마다 번호가 작은 것 부터 순서대로 상하좌우로 인접한 칸으로 퍼져나간다.
# s초 동안 바이러스가 퍼진 후에 (x, y) 에 있는 바이러스의 번호를 구하는 문제
# 단, 바이러스가 존재하지 않을 경우 0을 출력한다.
def sol18405():
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    s, x, y = map(int, input().split())

    q = []

    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                continue
            q.append((board[i][j], i, j))
    q.sort()

    for _ in range(s):
        if not q:
            break
        nq = []
        for v, r, c in q:
            if r > 0:
                nr, nc = r - 1, c
                if not board[nr][nc]:
                    board[nr][nc] = v
                    nq.append((v, nr, nc))
            if r < n - 1:
                nr, nc = r + 1, c
                if not board[nr][nc]:
                    board[nr][nc] = v
                    nq.append((v, nr, nc))
            if c > 0:
                nr, nc = r, c - 1
                if not board[nr][nc]:
                    board[nr][nc] = v
                    nq.append((v, nr, nc))
            if c < n - 1:
                nr, nc = r, c + 1
                if not board[nr][nc]:
                    board[nr][nc] = v
                    nq.append((v, nr, nc))
        q = nq
    return board[x - 1][y - 1]
