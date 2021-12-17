import sys

input = sys.stdin.readline
directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]


# 2615 오목
# 19 * 19 오목판 위에서 승자가 있는지 확인하고 있다면
# 이긴쪽과 완성된 오목의 좌측 상단의 바둑알의 좌표를 구하는 문제
def sol2615():
    board = [list(map(int, input().split())) for _ in range(19)]
    for i in range(19):
        for j in range(19):
            if board[i][j]:
                # 가로방향 체크
                w, r, c = check_five(board, i, j, 0)
                if w:
                    return '%d\n%d %d' % (w, r, c)

                # 세로방향 체크
                w, r, c = check_five(board, i, j, 1)
                if w:
                    return '%d\n%d %d' % (w, r, c)

                # 대각선방향1 체크
                w, r, c = check_five(board, i, j, 2)
                if w:
                    return '%d\n%d %d' % (w, r, c)

                # 대각선방향2 체크
                w, r, c = check_five(board, i, j, 3)
                if w:
                    return '%d\n%d %d' % (w, r, c)
    return 0


def check_five(board, r, c, d):
    p = board[r][c]
    v = directions[d]
    cnt = 1
    lr, lc = 0, 0

    # 왼쪽(세로일 경우 위쪽) 방향으로 탐색
    nr, nc = r - v[0], c - v[1]
    while 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == p:
        cnt += 1
        nr, nc = nr - v[0], nc - v[1]
    lr, lc = nr + v[0], nc + v[1]

    # 오른쪽(세로일 경우 아래쪽) 방향으로 탐색
    nr, nc = r + v[0], c + v[1]
    while 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == p:
        cnt += 1
        nr, nc = nr + v[0], nc + v[1]

    return (0, 0, 0) if cnt != 5 else (p, lr+1, lc+1)
