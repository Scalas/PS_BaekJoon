import sys

input = sys.stdin.readline
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# 10026 적록색약
# R, G, B 의 색으로 구성된 격자지도에서 R과 G를 구분하지 못하는 사람과 구분할 수 있는 사람이 봤을 때
# 지도 내의 영역의 갯수를 구하는 문제
def sol10026():
    # bfs 함수
    def bfs(i, j):
        q = [(i, j)]
        color = board[i][j]
        visited[i][j] = True
        while q:
            nq = []
            for r, c in q:
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and board[nr][nc] == color:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
            q = nq

    n = int(input())
    board = [list(input().rstrip()) for _ in range(n)]

    # 적록색약이 아닌사람 기준으로 영역의 갯수를 구한다
    visited = [[False] * n for _ in range(n)]
    c1 = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                c1 += 1

    # 적록색약인 사람 기준으로 영역의 갯수를 구한다
    visited = [[False] * n for _ in range(n)]
    c2 = 0
    # 지도의 G를 모두 R로 변경
    for line in board:
        for i in range(n):
            if line[i] == 'G':
                line[i] = 'R'
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                c2 += 1
    return '{} {}'.format(c1, c2)
