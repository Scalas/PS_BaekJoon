import sys

input = sys.stdin.readline


def sol1938():
    # 방향
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 입력
    n = int(input())
    board = [list(input().rstrip()) for _ in range(n)]

    # 통나무의 초기상태와 목적지(중심의 좌표, 방향: 가로 0 세로 1) 탐색
    # 통나무가 있던 자리와 목적지도 모두 '0'으로
    q = []
    visited = [[[0] * 2 for _ in range(n)] for _ in range(n)]
    bcheck, echeck = False, False
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'B':
                if bcheck:
                    board[i][j] = '0'
                    continue
                if i < n - 1 and board[i+1][j] == 'B':
                    q.append((i + 1, j, 1))
                    visited[i + 1][j][1] = 1
                else:
                    q.append((i, j + 1, 0))
                    visited[i][j + 1][0] = 1
                board[i][j] = '0'
                bcheck = True
            elif board[i][j] == 'E':
                if echeck:
                    board[i][j] = '0'
                    continue
                if i < n - 1 and board[i+1][j] == 'E':
                    visited[i + 1][j][1] = 2
                else:
                    visited[i][j + 1][0] = 2
                board[i][j] = '0'
                echeck = True

    # 이동횟수
    answer = 0

    while q:
        # 이동횟수 증가
        answer += 1
        nq = []
        for r, c, s in q:
            # 통나무가 가로 상태일 때
            if not s:
                # U
                if r > 0 and board[r-1][c-1] == board[r-1][c] == board[r-1][c+1] == '0':
                    nr, nc, ns = r - 1, c, s
                    if visited[nr][nc][ns] == 2:
                        return answer
                    if not visited[nr][nc][ns]:
                        visited[nr][nc][ns] = 1
                        nq.append((nr, nc, ns))
                # D
                if r < n-1 and board[r+1][c-1] == board[r+1][c] == board[r+1][c+1] == '0':
                    nr, nc, ns = r + 1, c, s
                    if visited[nr][nc][ns] == 2:
                        return answer
                    if not visited[nr][nc][ns]:
                        visited[nr][nc][ns] = 1
                        nq.append((nr, nc, ns))
                # L
                if c > 1 and board[r][c-2] == '0':
                    nr, nc, ns = r, c - 1, s
                    if visited[nr][nc][ns] == 2:
                        return answer
                    if not visited[nr][nc][ns]:
                        visited[nr][nc][ns] = 1
                        nq.append((nr, nc, ns))
                # R
                if c < n-2 and board[r][c+2] == '0':
                    nr, nc, ns = r, c + 1, s
                    if visited[nr][nc][ns] == 2:
                        return answer
                    if not visited[nr][nc][ns]:
                        visited[nr][nc][ns] = 1
                        nq.append((nr, nc, ns))
                # T
                if 0 < r < n-1 and board[r-1][c-1] == board[r-1][c] == board[r-1][c+1] == board[r+1][c-1] == board[r+1][c] == board[r+1][c+1] == '0':
                    nr, nc, ns = r, c, 1-s
                    if visited[nr][nc][ns] == 2:
                        return answer
                    if not visited[nr][nc][ns]:
                        visited[nr][nc][ns] = 1
                        nq.append((nr, nc, ns))

            # 통나무가 세로 상태일 때
            else:
                # U
                if r > 1 and board[r-2][c] == '0':
                    nr, nc, ns = r - 1, c, s
                    if visited[nr][nc][ns] == 2:
                        return answer
                    if not visited[nr][nc][ns]:
                        visited[nr][nc][ns] = 1
                        nq.append((nr, nc, ns))
                # D
                if r < n-2 and board[r+2][c] == '0':
                    nr, nc, ns = r + 1, c, s
                    if visited[nr][nc][ns] == 2:
                        return answer
                    if not visited[nr][nc][ns]:
                        visited[nr][nc][ns] = 1
                        nq.append((nr, nc, ns))
                # L
                if c > 0 and board[r-1][c-1] == board[r][c-1] == board[r+1][c-1] == '0':
                    nr, nc, ns = r, c - 1, s
                    if visited[nr][nc][ns] == 2:
                        return answer
                    if not visited[nr][nc][ns]:
                        visited[nr][nc][ns] = 1
                        nq.append((nr, nc, ns))
                # R
                if c < n-1 and board[r-1][c+1] == board[r][c+1] == board[r+1][c+1] == '0':
                    nr, nc, ns = r, c + 1, s
                    if visited[nr][nc][ns] == 2:
                        return answer
                    if not visited[nr][nc][ns]:
                        visited[nr][nc][ns] = 1
                        nq.append((nr, nc, ns))
                # T
                if 0 < c < n-1 and board[r-1][c-1] == board[r][c-1] == board[r+1][c-1] == board[r-1][c+1] == board[r][c+1] == board[r+1][c+1] == '0':
                    nr, nc, ns = r, c, 1-s
                    if visited[nr][nc][ns] == 2:
                        return answer
                    if not visited[nr][nc][ns]:
                        visited[nr][nc][ns] = 1
                        nq.append((nr, nc, ns))
        q = nq
    return 0
