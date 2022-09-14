import sys

input = sys.stdin.readline
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 18809 Gaaaaaaaaaarden
# n * m 격자공간에 호수(0)와 배양액을 뿌릴 수 없는 땅(1), 뿌릴 수 있는 땅(2) 이 주어지고
# r개의 빨간 배양액과 g 개의 초록 배양액을 배양액을 뿌릴 수 있는 땅에 임의로 뿌린 후
# 1초마다 배양액이 인접한 배양액이 없는 칸으로 퍼져나가며
# 동시에 두 색의 배양액이 퍼진 땅에선 꽃이 피어나고
# 꽃이 핀 땅에선 더이상 배양액이 퍼져나가지 않는다고 할 때
# 피어나는 꽃의 갯수의 최댓값을 구하는 문제
def sol18809():
    n, m, green, red = map(int, input().split())
    total_fluid = green + red
    board = [list(map(int, input().split())) for _ in range(n)]

    # 배양액을 뿌릴 수 있는 땅의 좌표 리스트
    available_ground = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                available_ground.append((i, j))
    total_ground = len(available_ground)

    # 뿌려진 배양액의 좌표와 색
    fluid = []

    # 배양액이 모두 뿌려졌을 때 배양이 퍼져나가는 것을 시뮬레이션하여 피어난 꽃의 갯수를 구하는 함수
    def simulate():
        q = fluid
        visited = [[0] * m for _ in range(n)]
        color = [[0] * m for _ in range(n)]
        turn = 1
        for r, c, t in q:
            visited[r][c] = turn
            color[r][c] = t

        flower = 0
        while q:
            turn += 1
            nq = []
            for r, c, t in q:
                # 꽃이 핀 장소에서는 더이상 퍼져나가지 않음
                if color[r][c] == 3:
                    flower += 1
                    continue

                # 배양액 확산
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc

                    # 땅의 범위를 벗어난 경우
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue

                    # 호수인 경우
                    if not board[nr][nc]:
                        continue

                    # 이미 확산된 경우
                    if visited[nr][nc]:
                        # 이전 턴에 확산됐다면 건너뜀
                        if visited[nr][nc] < turn:
                            continue

                        # 이번 턴에 확산됐다면 겹침
                        else:
                            color[nr][nc] |= t
                            continue

                    visited[nr][nc] = turn
                    color[nr][nc] = t
                    nq.append((nr, nc, t))
            q = nq

        return flower

    # 남은 용액의 수
    remain_fluid = total_fluid

    # 배양액을 뿌릴 위치를 배치하는 함수
    def inject(cur_ground):
        nonlocal remain_fluid, red, green

        # 모든 배양액을 뿌린 경우 시뮬레이션 실행
        if not remain_fluid:
            return simulate()

        # 현재 땅의 좌표
        cr, cc = available_ground[cur_ground]

        res = 0

        # 이번 땅에 배양액을 뿌리지 않아도 남은 배양액을 모두 뿌릴 수 있을 경우
        if total_ground - cur_ground > remain_fluid:
            res = inject(cur_ground + 1)

        # 빨간 배양액이 남아있는 경우
        if red:
            red -= 1
            fluid.append((cr, cc, 1))
            remain_fluid -= 1
            res = max(res, inject(cur_ground + 1))
            remain_fluid += 1
            fluid.pop()
            red += 1

        # 초록 용액이 남아있는 경우
        if green:
            green -= 1
            fluid.append((cr, cc, 2))
            remain_fluid -= 1
            res = max(res, inject(cur_ground + 1))
            remain_fluid += 1
            fluid.pop()
            green += 1

        return res

    return inject(0)
