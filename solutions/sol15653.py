import sys

input = sys.stdin.readline


# 15653 구슬 탈출 4
# n * m 격자공간상에 빨간구슬, 파란구슬, 구멍이 있을 때
# 격자를 상하좌우로 기울여 빨간구슬만을 구멍에 넣기 위해 격자를 기울여야할 최소 횟수를 구하는 문제
# 단, 파란구슬이 구멍에 들어가면 실패이다.
def sol15653():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]

    # 빨간구슬, 파란구슬의 위치
    red_row, red_col, blue_row, blue_col = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'B':
                blue_row, blue_col = i, j
                board[i][j] = '.'
            elif board[i][j] == 'R':
                red_row, red_col = i, j
                board[i][j] = '.'

    # 이동 방향별 벡터
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 이동 방향별로 빨간구슬이 먼저 움직여야하는지 여부를 구하는 함수 리스트
    should_red_first = [
        lambda r1, c1, r2, c2: (c1 == c2 and r1 < r2),
        lambda r1, c1, r2, c2: (r1 == r2 and c1 > c2),
        lambda r1, c1, r2, c2: (c1 == c2 and r1 > r2),
        lambda r1, c1, r2, c2: (r1 == r2 and c1 < c2)
    ]

    # 빨간구슬, 파란구슬의 좌표와 이동 방향이 주어졌을 때
    # 이동 후 빨간구슬, 파란구슬의 좌표를 반환하는 함수
    def move(r1, c1, r2, c2, d):
        dr, dc = direction[d]
        # 빨간 구슬이 먼저 이동해야하는 경우
        if should_red_first[d](r1, c1, r2, c2):
            while board[r1 + dr][c1 + dc] != '#':
                if board[r1 + dr][c1 + dc] == 'O':
                    r1, c1 = -1, -1
                    break
                r1, c1 = r1 + dr, c1 + dc
            while board[r2 + dr][c2 + dc] != '#':
                if board[r2 + dr][c2 + dc] == 'O':
                    r2, c2 = -1, -1
                    break
                if r2 + dr == r1 and c2 + dc == c1:
                    break
                r2, c2 = r2 + dr, c2 + dc
        # 그렇지 않은 경우
        else:
            while board[r2 + dr][c2 + dc] != '#':
                if board[r2 + dr][c2 + dc] == 'O':
                    r2, c2 = -1, -1
                    break
                r2, c2 = r2 + dr, c2 + dc
            while board[r1 + dr][c1 + dc] != '#':
                if board[r1 + dr][c1 + dc] == 'O':
                    r1, c1 = -1, -1
                    break
                if r1 + dr == r2 and c1 + dc == c2:
                    break
                r1, c1 = r1 + dr, c1 + dc

        return r1, c1, r2, c2

    # bfs로 빨간구슬만이 구멍에 들어가기 위해 격자를 기울여야 할 최소 횟수를 구함
    visited = set()
    q = [(red_row, red_col, blue_row, blue_col)]
    visited.add(q[0])
    answer = 0
    while q:
        answer += 1
        nq = []
        for rr, rc, br, bc in q:
            for d in range(4):
                after_move = move(rr, rc, br, bc, d)
                if after_move in visited:
                    continue

                visited.add(after_move)
                if after_move[2] == -1:
                    continue
                if after_move[0] == -1:
                    return answer
                nq.append(after_move)
        q = nq

    return -1
