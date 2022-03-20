import sys

input = sys.stdin.readline


# 6087 레이저 통신
# n * m 격자공간에 두 개의 C가 있고 한쪽 C에서 쏜 레이저가 다른쪽 C에 닿도록 거울을 배치하려 할 때
# 배치해야할 거울의 최소 갯수를 구하는 문제
def sol6087():
    m, n = map(int, input().split())
    board = [list(input()) for _ in range(n)]

    # bfs를 위한 큐
    q = []

    # 처음으로 찾은 C의 위치를 큐에 삽입
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'C':
                board[i][j] = 'x'
                q.append((i, j))
                break
        if q:
            break

    answer = -1
    while q:
        answer += 1
        nq = []
        for r, c in q:
            nr, nc = r, c
            while nr > 0 and board[nr][nc] != '*':
                nr -= 1
                if board[nr][nc] == '.':
                    board[nr][nc] = 'x'
                    nq.append((nr, nc))
                elif board[nr][nc] == 'C':
                    return answer

            nr, nc = r, c
            while nr < n-1 and board[nr][nc] != '*':
                nr += 1
                if board[nr][nc] == '.':
                    board[nr][nc] = 'x'
                    nq.append((nr, nc))
                elif board[nr][nc] == 'C':
                    return answer

            nr, nc = r, c
            while nc > 0 and board[nr][nc] != '*':
                nc -= 1
                if board[nr][nc]=='.':
                    board[nr][nc] = 'x'
                    nq.append((nr, nc))
                elif board[nr][nc] == 'C':
                    return answer

            nr, nc = r, c
            while nc < m-1 and board[nr][nc] != '*':
                nc += 1
                if board[nr][nc]=='.':
                    board[nr][nc] = 'x'
                    nq.append((nr, nc))
                elif board[nr][nc] == 'C':
                    return answer
        q = nq

    return -1
