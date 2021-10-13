import sys

input = sys.stdin.readline
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# 2583 영역 구하기
# 모눈종이 위에 주어진 좌표에따라 사각형을 그렸을 때
# 나눠진 빈 영역의 갯수와 각 영역의 넓이를 구하는 문제
def sol2583():
    m, n, k = map(int, input().split())
    board = [[0] * (m + 2) for _ in range(n + 2)]

    # 주어진 좌표를 기반으로 모눈종이상에 사각형 영역을 표시
    # 누적합을 사용하여 O(K+NM) 으로 해결한다
    for _ in range(k):
        u, v, w, x = map(int, input().split())
        board[u][v] += 1
        board[w][x] += 1
        board[w][v] -= 1
        board[u][x] -= 1

    for i in range(n + 1):
        for j in range(m + 1):
            board[i + 1][j] += board[i][j]
            board[i][j] += board[i][j - 1]

    # bfs 를 사용하여 나눠진 빈 영역의 갯수와 넓이를 구한다
    cnt = 0
    area = []
    for i in range(n):
        for j in range(m):
            if not board[i][j]:
                area.append(bfs(board, n, m, i, j))
                cnt += 1

    # 영역의 넓이를 오름차순 정렬
    area.sort()

    return '{}\n{}'.format(cnt, ' '.join(map(str, area)))


# bfs 함수
def bfs(board, n, m, i, j):
    size = 0
    q = [(i, j)]
    board[i][j] = 1
    while q:
        nq = []
        for r, c in q:
            size += 1
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not board[nr][nc]:
                    board[nr][nc] = 1
                    nq.append((nr, nc,))
        q = nq
    return size

