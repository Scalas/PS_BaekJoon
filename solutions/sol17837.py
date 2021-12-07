import sys

input = sys.stdin.readline
directions = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]


# 17837 새로운 게임 2
# n * n 체스판 위에서 k개의 말이 규칙에 따라 이동한다
# 1. 1턴이 진행되면 1 번부터 k 번까지 말들이 순차적으로 이동을 진행한다.
# 2. 이동방향은 좌, 우, 상, 하 네가지이며 각각 1, 2, 3, 4로 표현한다.
# 3. 말은 이동할 때 자신의 위에 쌓인 말들과 함께 이동한다.
# 4. 이동할 위치에 이미 말이 존재할 경우 그 위에 쌓인다.
# 5. 체스판에는 색이 칠해져있다 (0: 흰색, 1: 붉은색, 2: 푸른색)
# 6. 이동할 칸이 체스판을 벗어나거나 푸른색이라면 방향을 반대로 하여 다시 이동을 시도한다.
#    만약 반대방향으로 이동할 칸도 체스판을 벗어나거나 푸른색이라면 이동하지 않는다.
# 7. 이동할 칸이 흰색이라면 해당 위치로 이동한다.
# 8. 이동할 칸이 붉은색이라면 해당 위치로 이동한 뒤 이동한 말을 포함한 그 위쪽의 말들의 순서를 뒤집는다.
# 9. 4개이상 쌓인 말이 생길 경우 게임은 종료된다.

# 보드의 크기와 말의 갯수, 보드의 상태와 말들의 위치, 방향 정보가 주어졌을 때
# 게임이 1000 이하의 턴수로 종료될 경우 종료된 턴 수를, 그렇지 않을 경우 -1을 반환하는 문제.
def sol17837():
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    board_st = [[list() for _ in range(n)] for _ in range(n)]
    chips = []
    for i in range(k):
        r, c, d = map(int, input().split())
        chips.append([r-1, c-1, d])
        board_st[r-1][c-1].append(i)

    # 말 이동 함수
    def move(chip_num, changed):
        r, c, d = chips[chip_num]

        nr, nc = r + directions[d][0], c + directions[d][1]
        # 이동하려는 칸이 보드를 벗어나지 않고 푸른색이 아닌경우
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 2:
            # 현재 칸에서의 이동하려는 말의 위치 탐색
            idx = board_st[r][c].index(chip_num)

            # 이동하려는 말과 그 위의 말들을 현재 칸에서 분리, 말들의 위치를 목적지로 변경
            board_st[r][c], tmp = board_st[r][c][:idx], board_st[r][c][idx:]
            for cn in tmp:
                chips[cn][0], chips[cn][1] = nr, nc

            # 이동하려는 칸이 붉은색일 경우 이동할 말들의 순서 뒤집기
            if board[nr][nc]:
                tmp = tmp[::-1]

            # 이동하려는 칸 위에 쌓기
            board_st[nr][nc].extend(tmp)

            # 쌓인 말의 수가 4개 이상이라면 True, 아니라면 False 반환
            return len(board_st[nr][nc]) >= 4

        # 이동하려는 칸이 보드를 벗어나거나 푸른색인 경우
        else:
            # 이미 반대방향으로 전환한 상태일 경우 이동 종료
            if changed:
                return

            # 반대방향으로 전환하여 재이동
            chips[chip_num][2] = d + (1 if d % 2 else -1)
            return move(chip_num, True)

    # 게임이 종료될 때 까지(말이 4개이상 쌓일 때 까지) 반복
    turn = 0
    while True:
        turn += 1
        if turn > 1000:
            break

        check = False
        for i in range(k):
            if move(i, False):
                check = True
                break
        if check:
            break

    # 1000 이하의 턴수로 종료됐다면 종료 턴수를, 아니라면 -1을 반환
    return turn if turn <= 1000 else -1
