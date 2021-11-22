import sys

input = sys.stdin.readline


# 2638 치즈
# n * m 격자맵에서 0은 치즈가 없는곳, 1은 치즈가 있는곳이며
# 가장자리와 연결된 0 부분은 공기라고 할 때(치즈로 둘러쌓인 0은 진공상태)
# 공기가 두 면 이상이 맞닿은 치즈는 한시간만에 녹는다
# 이 때 모든 치즈가 녹기 위해 필요한 시간을 구하는 문제
def sol2638():
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    n, m = map(int, input().split())

    # 치즈의 갯수
    cheese = 0

    board = []
    for _ in range(n):
        line = [*map(int, input().split())]
        cheese += line.count(1)
        board.append(line)

    # 공기를 -1로 변경
    q = [(0, 0)]
    board[0][0] = -1
    while q:
        nq = []
        for r, c in q:
            for rd, cd in d:
                nr, nc = r + rd, c + cd
                if 0 <= nr < n and 0 <= nc < m and not board[nr][nc]:
                    board[nr][nc] = -1
                    nq.append((nr, nc))
        q = nq

    # 치즈가 사라질 때 까지
    t = 0
    while cheese:
        # 공기(-1)에 인접한 모든 치즈는 녹은 치즈 리스트(q)에 자기자신을 추가하고
        # 모눈종이상에서 0이되어 사라지며 치즈갯수를 1 감소시킨다.
        q = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    cnt = 0
                    for rd, cd in d:
                        ni, nj = i + rd, j + cd
                        if 0 <= ni < n and 0 <= nj < m and board[ni][nj] < 0:
                            cnt += 1
                    if cnt >= 2:
                        q.append((i, j))
                        board[i][j] = 0
                        cheese -= 1

        # 이번에 녹은 치즈를 기점으로 공기를 -1로 치환
        for r, c in q:
            board[r][c] = -1
        while q:
            nq = []
            for r, c in q:
                for rd, cd in d:
                    nr, nc = r + rd, c + cd
                    if 0 <= nr < n and 0 <= nc < m and not board[nr][nc]:
                        board[nr][nc] = -1
                        nq.append((nr, nc))
            q = nq

        # 시간 1 증가
        t += 1

    # 치즈가 모두 녹는데 걸린 시간 반환
    return t


