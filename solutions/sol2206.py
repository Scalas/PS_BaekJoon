import sys

input = sys.stdin.readline


# 2206 벽 부수고 이동하기
# 미로찾기의 응용문제
# 기존의 최단거리 찾기와 달리 벽을 부수는 경우를 별도로 따져볼 필요가있음
def sol2206():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    nw = {'0', '2'}
    q = [(0, 0, 2)]
    answer = 1
    while q:
        nq = []
        for r, c, w in q:
            if r == n - 1 and c == m - 1:
                return answer

            for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] != '3':
                    if w == 1:
                        if board[nr][nc] == '0':
                            board[nr][nc] = '2'
                            nq.append((nr, nc, 1))
                    else:
                        if board[nr][nc] == '1':
                            nq.append((nr, nc, 1))
                        elif board[nr][nc] in nw:
                            nq.append((nr, nc, 2))
                        board[nr][nc] = '3'
        answer += 1
        q = nq
    return -1
