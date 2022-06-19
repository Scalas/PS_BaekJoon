import sys

input = sys.stdin.readline


# 13459 구슬 탈출
# n * m 격자공간에 벽(#), 빈공간(.), 구멍(O)의 위치가 주어지고
# 처음 빨간 구슬과 파란 구슬의 위치가 주어졌을 때
# 격자를 상하좌우로 최대 10회 기울여 빨간공만 구멍으로 빠져나가도록 할 수 있는지 여부를 구하는 문제
def sol13459():
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]

    # 빨간구슬, 파란구슬의 위치 파악
    rr, rc, br, bc = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rr, rc = i, j
                board[i][j] = '.'
            elif board[i][j] == 'B':
                br, bc = i, j
                board[i][j] = '.'

    # bfs로 모든 경우 탐색
    visited = set()
    q = [(rr, rc, br, bc)]
    visited.add(q[0])
    cnt = 0
    while q and cnt < 10:
        nq = []
        cnt += 1
        for rr, rc, br, bc in q:
            for i in range(4):
                dr, dc = direction[i]
                # 어느 구슬이 먼저 움직여야할지 정하는 값
                # 0이면 빨강이 먼저, 1이면 파랑이 먼저
                turn = 0
                # 상하좌우와 빨간구슬, 파란구슬의 위치에 따라 이동 순서를 정함
                if i == 0:
                    turn = 0 if rc > bc else 1
                elif i == 1:
                    turn = 0 if rc < bc else 1
                elif i == 2:
                    turn = 0 if rr > br else 1
                else:
                    turn = 0 if rr < br else 1

                # 이동 결과
                rnr, rnc, bnr, bnc = rr, rc, br, bc

                # 파란구슬이 우선일 경우
                if turn:
                    # 파란구슬을 이동방향으로 벽을 만날 때 까지 이동
                    while board[bnr + dr][bnc + dc] != '#':
                        bnr += dr
                        bnc += dc
                        # 중간에 구멍에 빠질 경우 좌표를 -1, -1로 함
                        if board[bnr][bnc] == 'O':
                            bnr, bnc = -1, -1

                    # 빨간구슬을 이동방향으로 벽 또는 파란구슬을 만날 때 까지 이동
                    while board[rnr + dr][rnc + dc] != '#' and (rnr + dr != bnr or rnc + dc != bnc):
                        rnr += dr
                        rnc += dc
                        # 중간에 구멍에 빠질 경우 좌표를 -1, -1로 함
                        if board[rnr][rnc] == 'O':
                            rnr, rnc = -1, -1

                    # 빨간구슬만 구멍에 빠진경우
                    if rnr == -1 and bnr != -1:
                        return 1

                    # 둘 다 빠지지 않았고 아직 방문하지 않은 상태일 경우 큐에 삽입
                    state = (rnr, rnc, bnr, bnc)
                    if rnr != -1 and bnr != -1 and state not in visited:
                        nq.append(state)
                        visited.add(state)

                # 빨간구슬이 우선일 경우
                else:
                    # 빨간구슬을 이동방향으로 벽을 만날 때 까지 이동
                    while board[rnr + dr][rnc + dc] != '#':
                        rnr += dr
                        rnc += dc
                        # 중간에 구멍에 빠질 경우 좌표를 -1, -1로 함
                        if board[rnr][rnc] == 'O':
                            rnr, rnc = -1, -1

                    # 파란구슬을 이동방향으로 벽 또는 빨간구슬을 만날 때 까지 이동
                    while board[bnr + dr][bnc + dc] != '#' and (bnr + dr != rnr or bnc + dc != rnc):
                        bnr += dr
                        bnc += dc
                        # 중간에 구멍에 빠질 경우 좌표를 -1, -1로 함
                        if board[bnr][bnc] == 'O':
                            bnr, bnc = -1, -1

                    # 빨간구슬만 구멍에 빠진경우
                    if rnr == -1 and bnr != -1:
                        return 1

                    # 둘 다 빠지지 않았고 아직 방문하지 않은 상태일 경우 큐에 삽입
                    state = (rnr, rnc, bnr, bnc)
                    if rnr != -1 and bnr != -1 and state not in visited:
                        nq.append(state)
                        visited.add(state)
        q = nq

    # 더이상 구슬을 움직일 경우의 수가 없거나 10회 넘게 이동하도록
    # 빨간구슬만을 빼내지 못했을 경우
    return 0
