import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
direction = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


# 19236 청소년 상어
# 4 * 4 공간에 한칸당 한마리씩 물고기가 존재
# 물고기의 번호는 1 ~ 16번으로 중복되지않으며 각 물고기는 초기에 방향을 가지고있음
# 상어는 처음에 (0, 0)으로 이동하여 물고기를 잡아먹고 그 방향을 이어받는다
# 이후 다음의 과정이 반복된다
# 1. 물고기는 각각 초기에 지정된 방향으로 1칸씩 이동한다. 빈칸일 경우 그냥 이동, 물고기가 있을 경우
#    그자리에 있는 물고기와 자리를 교환, 상어가있거나 공간을 벗어날 경우 이동할 수 없다.
#    이동할 수 있는 방향이 없다면 이동하지 않는다.
#
# 2. 물고기가 모두 이동하고나면 상어는 이전에 물고기를 잡아먹어 변경된 자신의 방향으로 이동한다.
#    상어의 이동 칸수에는 제약이 없으나 물고기가 없는 칸으로는 이동할 수 없으며 만약 경로에
#    물고기가 있는 칸이 하나도 없다면 상어는 그대로 공간을 빠져나가고 시뮬레이션은 종료된다.
#
# 위 과정을 상어가 공간을 빠져나갈 때 까지 반복하여 상어가 먹을 수 있는 모든 물고기의 번호의 합 중 최댓값을 구하는 문제
def sol19236():
    space = []
    fish = [[0] * 3 for _ in range(17)]
    for i in range(4):
        s, t, u, v, w, x, y, z = map(int, input().split())
        fish[s] = [t, i, 0]
        fish[u] = [v, i, 1]
        fish[w] = [x, i, 2]
        fish[y] = [z, i, 3]
        space.append([s, u, w, y])

    def shark(sr, sc, sd):
        nonlocal space, fish

        # 물고기 이동 전 상태 백업
        bspace = [space[i][:] for i in range(4)]
        bfish = [fish[i][:] for i in range(17)]

        # 물고기의 이동
        for i in range(1, 17):
            fd, fr, fc = fish[i]
            # 방향값이 0이 아니라면(먹히지 않았다면)
            if fd:
                # 이동 가능한 칸(빈 공간이거나 물고기가 있는 칸)을 탐색
                check = False
                nfr, nfc = 0, 0
                # 현재 방향으로 이동 불가능하다면 반시계방향으로 45도씩 돌려가며 탐색
                for _ in range(8):
                    nfr, nfc = fr + direction[fd][0], fc + direction[fd][1]
                    if 0 <= nfr < 4 and 0 <= nfc < 4 and space[nfr][nfc] >= 0:
                        check = True
                        break
                    fd += 1
                    if fd == 9:
                        fd = 1

                # 이동 가능한 경우
                if check:
                    # 이동할 칸의 상태
                    target = space[nfr][nfc]

                    # 물고기가 있는 칸인 경우
                    if space[nfr][nfc]:
                        # 정보 수정
                        fish[target][1], fish[target][2] = fr, fc
                        fish[i] = [fd, nfr, nfc]

                        # 위치교환
                        space[fr][fc], space[nfr][nfc] = space[nfr][nfc], space[fr][fc]

                    # 빈칸인 경우
                    else:
                        # 정보 수정
                        fish[i] = [fd, nfr, nfc]

                        # 위치 이동
                        space[fr][fc], space[nfr][nfc] = 0, space[fr][fc]

        # 상어의 이동
        # 상어가 이동할수 있는 모든 경우중 먹은 물고기의 합이 가장 큰 경우를 탐색
        # 이동할 수 없다면 0을 반환하게 된다.
        res = 0

        # 초기이동, 처음 있던칸은 빈칸으로
        space[sr][sc] = 0
        sr, sc = sr + direction[sd][0], sc + direction[sd][1]

        # 상어가 이동할 공간이 공간을 벗어나지 않는동안
        while 0 <= sr < 4 and 0 <= sc < 4:
            # 물고기가 존재하는 칸이 있다면 이동해본다
            if space[sr][sc]:
                # 잡아먹힌 물고기의 번호, 방향
                eat_num = space[sr][sc]
                eat_d = fish[eat_num][0]

                # 물고기가 잡아먹혔음을 표시
                # 해당 칸에 상어가 있음을 표시
                fish[eat_num][0] = 0
                space[sr][sc] = -1

                # 다음 단계로 이행, 먹은 물고기의 번호의 합의 최댓값을 갱신
                res = max(res, shark(sr, sc, eat_d) + eat_num)

                # 이동전 상태로 복구
                fish[eat_num][0] = eat_d
                space[sr][sc] = eat_num

            # 다른 칸을 탐색
            sr, sc = sr + direction[sd][0], sc + direction[sd][1]

        # 상태 복구
        space, fish = bspace, bfish

        # 먹은 물고기의 번호의 합의 최댓값 반환
        return res

    # 상어가 공간에 진입
    sr, sc = 0, 0
    eat_num = space[sr][sc]
    sd, fish[eat_num][0] = fish[eat_num][0], 0
    space[sr][sc] = -1

    # 상어가 먹은 물고기의 번호의 합의 최댓값을 반환
    return shark(sr, sc, sd) + eat_num
