import sys

input = sys.stdin.readline
INF = 100


# 25368 사과를 더 많이 먹자
# 5 * 5 보드상에 사과(1), 빈공간(0), 장애물(-1) 이 있고 유저 두 명은 임의 위치에서 게임을 시작한다.
# 유저는 매 턴 자신이 먹는 사과 수 - 상대가 먹는 사과 수 가 최대가 되도록 최선의 수로 움직이고
# 유저가 방문한 칸은 유저가 떠나는 순간 장애물로 변하여 다시 올 수 없게 되며 다른 유저가 있는 칸으로는 움직일 수 없다.
# 본인 차례에 움직일 수 없다면 다른 유저가 계속해서 움직인다.
# 두 유저 모두 더이상 움직일 수 없거나 사과가 모두 사라지면 게임은 종료된다.
# 유저 1(r1, c1) -> 유저 2(r2, c2) 순으로 턴제로 게임을 진행할 때 유저 1이 먹은 사과의 수가
# 유저 2가 먹은 사과의 수 보다 많을 수 있다면 1, 아니라면 0 을 반환하는 문제
def sol25368():
    # board 의 초기 상태
    board = [list(map(int, input().split())) for _ in range(5)]
    apple = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                apple += 1

    # 유저들의 초기 위치, 먹은 사과 갯수
    row1, col1, row2, col2 = map(int, input().split())
    u1, u2 = 0, 0
    if board[row1][col1] == 1:
        u1 += 1
        apple -= 1
    if board[row2][col2] == 1:
        u2 += 1
        apple -= 1
    board[row1][col1] = board[row2][col2] = -1

    # 유저들이 움직일 수 있는 상태인지 여부
    u1_movable, u2_movable = True, True

    def dfs(r1, c1, r2, c2, turn):
        nonlocal u1, u2, apple, u1_movable, u2_movable

        # 두 유저 모두 움직일 수 없거나 사과가 모두 사라졌다면 게임 종료
        # 유저 1이 먹은 사과의 수 - 유저 2가 먹은 사과의 수를 반환
        if (not u1_movable and not u2_movable) or not apple:
            return u1 - u2

        # 유저 1의 차례
        if turn == 0:
            # u1 - u2 를 최대화하는 케이스를 반환
            max_diff = -INF

            # 상하좌우에 대해 장애물이 없다면 이동하고 그 자리에 장애물을 설치
            # 사과가 있다면 먹은 사과의 수를 1 증가시키고 다음 유저에게 턴을 넘김
            if u1_movable:
                if r1 > 0:
                    nr1, nc1 = r1 - 1, c1
                    if board[nr1][nc1] != -1:
                        org_val = board[nr1][nc1]
                        if org_val == 1:
                            u1 += 1
                            apple -= 1
                        board[nr1][nc1] = -1
                        max_diff = max(max_diff, dfs(nr1, nc1, r2, c2, 1 - turn))
                        board[nr1][nc1] = org_val
                        if org_val == 1:
                            u1 -= 1
                            apple += 1

                if r1 < 4:
                    nr1, nc1 = r1 + 1, c1
                    if board[nr1][nc1] != -1:
                        org_val = board[nr1][nc1]
                        if org_val == 1:
                            u1 += 1
                            apple -= 1
                        board[nr1][nc1] = -1
                        max_diff = max(max_diff, dfs(nr1, nc1, r2, c2, 1 - turn))
                        board[nr1][nc1] = org_val
                        if org_val == 1:
                            u1 -= 1
                            apple += 1
                if c1 > 0:
                    nr1, nc1 = r1, c1 - 1
                    if board[nr1][nc1] != -1:
                        org_val = board[nr1][nc1]
                        if org_val == 1:
                            u1 += 1
                            apple -= 1
                        board[nr1][nc1] = -1
                        max_diff = max(max_diff, dfs(nr1, nc1, r2, c2, 1 - turn))
                        board[nr1][nc1] = org_val
                        if org_val == 1:
                            u1 -= 1
                            apple += 1

                if c1 < 4:
                    nr1, nc1 = r1, c1 + 1
                    if board[nr1][nc1] != -1:
                        org_val = board[nr1][nc1]
                        if org_val == 1:
                            u1 += 1
                            apple -= 1
                        board[nr1][nc1] = -1
                        max_diff = max(max_diff, dfs(nr1, nc1, r2, c2, 1 - turn))
                        board[nr1][nc1] = org_val
                        if org_val == 1:
                            u1 -= 1
                            apple += 1

                # 움직일 수 없다면 movable 을 False 로 하고 다음 유저에게 턴을 넘김
                if max_diff == -INF:
                    u1_movable = False
                    max_diff = max(max_diff, dfs(r1, c1, r2, c2, 1 - turn))
                    u1_movable = True

                return max_diff

            # 움직일 수 없는 상태라면 아무 것도 하지 않고 다음 유저에게 턴을 넘김
            else:
                return dfs(r1, c1, r2, c2, 1 - turn)

        # 유저 2에 대해 위와 같은 절차 반복
        # 단, u1 - u2 를 최소화 하는 케이스를 반환
        else:
            min_diff = INF

            if u2_movable:
                if r2 > 0:
                    nr2, nc2 = r2 - 1, c2
                    if board[nr2][nc2] != -1:
                        org_val = board[nr2][nc2]
                        if org_val == 1:
                            u2 += 1
                            apple -= 1
                        board[nr2][nc2] = -1
                        min_diff = min(min_diff, dfs(r1, c1, nr2, nc2, 1 - turn))
                        board[nr2][nc2] = org_val
                        if org_val == 1:
                            u2 -= 1
                            apple += 1

                if r2 < 4:
                    nr2, nc2 = r2 + 1, c2
                    if board[nr2][nc2] != -1:
                        org_val = board[nr2][nc2]
                        if org_val == 1:
                            u2 += 1
                            apple -= 1
                        board[nr2][nc2] = -1
                        min_diff = min(min_diff, dfs(r1, c1, nr2, nc2, 1 - turn))
                        board[nr2][nc2] = org_val
                        if org_val == 1:
                            u2 -= 1
                            apple += 1

                if c2 > 0:
                    nr2, nc2 = r2, c2 - 1
                    if board[nr2][nc2] != -1:
                        org_val = board[nr2][nc2]
                        if org_val == 1:
                            u2 += 1
                            apple -= 1
                        board[nr2][nc2] = -1
                        min_diff = min(min_diff, dfs(r1, c1, nr2, nc2, 1 - turn))
                        board[nr2][nc2] = org_val
                        if org_val == 1:
                            u2 -= 1
                            apple += 1

                if c2 < 4:
                    nr2, nc2 = r2, c2 + 1
                    if board[nr2][nc2] != -1:
                        org_val = board[nr2][nc2]
                        if org_val == 1:
                            u2 += 1
                            apple -= 1
                        board[nr2][nc2] = -1
                        min_diff = min(min_diff, dfs(r1, c1, nr2, nc2, 1 - turn))
                        board[nr2][nc2] = org_val
                        if org_val == 1:
                            u2 -= 1
                            apple += 1

                if min_diff == INF:
                    u2_movable = False
                    min_diff = min(min_diff, dfs(r1, c1, r2, c2, 1 - turn))
                    u2_movable = True

                return min_diff

            else:
                return dfs(r1, c1, r2, c2, 1 - turn)

    res = dfs(row1, col1, row2, col2, 0)
    return 1 if res > 0 else 0
