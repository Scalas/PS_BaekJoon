import sys

input = sys.stdin.readline


# 21322 격자 돌리기
# n * n 모양 격자가 주어지고 바깥에서부터 한겹씩을 하나의 컨베이어 벨트라고 한다.
# 각 컨베이어 벨트에는 숫자가 하나씩 있고 컨베이어 벨트에 대해 다음 세 가지 명령을 수행할 수 있다.
# 1 a b : 바깥에서부터 a 번째 벨트를 b 번 시계방향 회전
# 2 c d : (c, d), (c, d + 1), (c + 1, d), (c + 1, d + 1) 네 칸을 시계방향으로 회전
# 3 e f : (e, f) 의 수를 출력
# 초기 격자의 상태와 명령이 주어졌을 때 명령을 m개 수행한 결과를 구하는 문제
def sol21322():
    n, m = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]

    # belt_idx[i][j] 는 격자상에서 (i, j)의 위치가 바깥에서 몇 번째 벨트의 몇 번째 위치에 해당하는지 매핑
    belt_idx = [[0] * n for _ in range(n)]

    # belt[i][j] 는 바깥에서 i 번째 벨트의 j 번째 수
    # 각 벨트의 첫 번째 수는 격자상에서의 왼쪽 위 모서리로 한다.
    belt = [[] for _ in range(n // 2)]
    for bidx in range(n // 2):
        sr, sc = bidx, bidx
        cidx = 0
        belt_idx[sr][sc] = (bidx, cidx)
        belt[bidx].append(board[sr][sc])
        cidx += 1
        side = n - 2 * bidx - 1
        for _ in range(side):
            sr += 1
            belt_idx[sr][sc] = (bidx, cidx)
            belt[bidx].append(board[sr][sc])
            cidx += 1
        for _ in range(side):
            sc += 1
            belt_idx[sr][sc] = (bidx, cidx)
            belt[bidx].append(board[sr][sc])
            cidx += 1
        for _ in range(side):
            sr -= 1
            belt_idx[sr][sc] = (bidx, cidx)
            belt[bidx].append(board[sr][sc])
            cidx += 1
        for _ in range(side - 1):
            sc -= 1
            belt_idx[sr][sc] = (bidx, cidx)
            belt[bidx].append(board[sr][sc])
            cidx += 1

    # 명령 수행
    # 2, 3 번 명령 수행시에는 cycle에 기록된 벨트 회전수를 반영하여 실제위치를 계산한다.
    answer = []
    cycle = [0] * (n // 2)
    pos = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for _ in range(m):
        cmd, arg1, arg2 = map(int, input().split())
        # 1번 회전명령 수행시 회전수를 증가
        if cmd == 1:
            cycle[arg1 - 1] = (cycle[arg1 - 1] + arg2) % len(belt[arg1 - 1])

        # 2번 회전명령 수행시 해당하는 네 수를 찾아 실제로 회전
        elif cmd == 2:
            eff_idx = []
            for pr, pc in pos:
                r, c = arg1 + pr - 1, arg2 + pc - 1
                bidx, cidx = belt_idx[r][c]
                cidx = (cidx + cycle[bidx]) % len(belt[bidx])
                eff_idx.append(bidx)
                eff_idx.append(cidx)

            belt[eff_idx[0]][eff_idx[1]], belt[eff_idx[2]][eff_idx[3]], belt[eff_idx[4]][eff_idx[5]], belt[eff_idx[6]][eff_idx[7]] = belt[eff_idx[4]][eff_idx[5]], belt[eff_idx[0]][eff_idx[1]], belt[eff_idx[6]][eff_idx[7]], belt[eff_idx[2]][eff_idx[3]]

        # 3번 출력명령 수행시 해당하는 수를 출력
        elif cmd == 3:
            bidx, cidx = belt_idx[arg1 - 1][arg2 - 1]
            cidx = (cidx + cycle[bidx]) % len(belt[bidx])
            answer.append(belt[bidx][cidx])

    return '\n'.join(map(str, answer))
