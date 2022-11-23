import sys

input = sys.stdin.readline


# 6593 상범 빌딩
# 3차원 격자공간에 벽(#)과 빈 공간(.), 시작점(S)과 출구(E)가 주어졌을 때
# 매 시간마다 전후좌우상하의 인접한 빈 공간으로만 이동하며 시작점에서 출구로 빠져나가기 위한 최단시간을 구하는 문제
# 만약 나갈 수 없을 경우 Trapped!를 출력
def sol6593():
    answers = []
    directions = [
        (0, 0, 1),
        (0, 0, -1),
        (0, 1, 0),
        (0, -1, 0),
        (1, 0, 0),
        (-1, 0, 0)
    ]
    while True:
        n, m, k = map(int, input().split())
        if n == m == k == 0:
            break
        board = []
        q = []
        er, ec, ex = 0, 0, 0
        for r in range(n):
            floor = [list(input().rstrip()) for _ in range(m)]
            for c in range(m):
                for x in range(k):
                    if floor[c][x] == 'S':
                        q.append((r, c, x))
                        floor[c][x] = '#'
                    else:
                        er, ec, ex = r, c, x
            input()
            board.append(floor)

        answer = 0
        check = False
        while q:
            nq = []
            answer += 1
            for cr, cc, cx in q:
                for dr, dc, dx in directions:
                    nr, nc, nx = cr + dr, cc + dc, cx + dx
                    if not (0 <= nr < n):
                        continue
                    if not (0 <= nc < m):
                        continue
                    if not (0 <= nx < k):
                        continue
                    if board[nr][nc][nx] == '#':
                        continue
                    if board[nr][nc][nx] == 'E':
                        answers.append(f'Escaped in {answer} minute(s).')
                        check = True
                        break
                    board[nr][nc][nx] = '#'
                    nq.append((nr, nc, nx))
                if check:
                    break
            if check:
                break
            q = nq

        if not check:
            answers.append('Trapped!')

    return '\n'.join(answers)
