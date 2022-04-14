import sys

input = sys.stdin.readline


def sol1194():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    key_bit = {'a': 1, 'b': 1 << 1, 'c': 1 << 2, 'd': 1 << 3, 'e': 1 << 4, 'f': 1 << 5}

    # 최단 이동거리 탐색
    def bfs(r, c):
        key_set = 0
        q = [(r, c, key_set)]

        # visited[key_set][i][j] 는 가지고있는 열쇠의 상태가 key_set일 때 (i, j)에 방문한적이 있는지 여부
        visited = [[[False] * m for _ in range(n)] for _ in range(64)]
        visited[key_set][r][c] = True
        dst = 0
        while q:
            nq = []
            for r, c, key_set in q:
                # 출구 도착시
                if board[r][c] == '1':
                    return dst

                # 상하좌우 이동
                for dr, dc in direction:
                    nr, nc, nkey_set = r + dr, c + dc, key_set

                    # 격자 밖일경우 진행불가
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue

                    # 벽일경우 진행불가
                    if board[nr][nc] == '#':
                        continue

                    # 열쇠가 없는 문일경우 진행불가
                    if board[nr][nc].isupper():
                        if not key_set & key_bit[board[nr][nc].lower()]:
                            continue

                    # 열쇠가 있을 경우 nkey_set에 추가
                    if board[nr][nc].islower():
                        nkey_set |= key_bit[board[nr][nc]]

                    # 이미 방문한경우 진행불가
                    if visited[nkey_set][nr][nc]:
                        continue

                    # 이동
                    visited[nkey_set][nr][nc] = True
                    nq.append((nr, nc, nkey_set))
            q = nq
            dst += 1
            
        # 목적지에 도달하지 못했을 경우 -1 반환
        return -1

    # 시작위치를 찾아 탐색시작
    for i in range(n):
        for j in range(m):
            if board[i][j] == '0':
                answer = bfs(i, j)
                return answer
