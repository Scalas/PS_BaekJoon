import sys

input = sys.stdin.readline


# 1926 그림
# n * m 도화지상에 빈 칸은 0, 그림이 그려진 칸은 1로 주어진다.
# 상하좌우로 이어진 칸은 하나의 그림이라고 할 때
# 그림의 갯수와 가장 큰 그림의 크기(칸의 갯수)를 구하는 문제
def sol1926():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    def bfs(r, c):
        q = [(r, c)]
        visited[r][c] = True
        size = 0
        while q:
            nq = []
            for cr, cc in q:
                size += 1
                if cr > 0:
                    nr, nc = cr - 1, cc
                    if not visited[nr][nc] and board[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                if cr < n - 1:
                    nr, nc = cr + 1, cc
                    if not visited[nr][nc] and board[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                if cc > 0:
                    nr, nc = cr, cc - 1
                    if not visited[nr][nc] and board[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                if cc < m - 1:
                    nr, nc = cr, cc + 1
                    if not visited[nr][nc] and board[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
            q = nq
        return size

    answer = [0, 0]
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue
            if visited[i][j]:
                continue
            answer[0] += 1
            answer[1] = max(answer[1], bfs(i, j))

    return '\n'.join(map(str, answer))
