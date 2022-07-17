import sys

input = sys.stdin.readline


# 23288 주사위 굴리기 2
# 1. n * m (2 <= n, m <= 20) 격자공간의 각 칸에는 10 미만의 자연수가 적혀있다
# 2. 주사위는 서로 마주보는 면의 합이 7이 되도록 만들어져있다.
# 3. 주사위는 처음에 (0, 0)에 위치하며 위쪽면은 1, 동쪽을 바라보는 면은 3인 상태로 놓여있다.
# 4. 주사위의 초기 이동방향은 동쪽이며 주사위가 이동한 후 밑면이 해당 칸의 수보다 크다면 시계 방향으로, 작다면 반시계 방향으로 이동 방향을 90도 회전한다. 같다면 회전하지 않는다.
# 5. 만약 이동할 방향으로 칸이 존재하지 않는다면 방향을 반대로 전환한다.
# 6. 주사위가 이동한 후에 얻게되는 점수는 해당 칸과 숫자가 같고 인접한 칸으로 이어진 칸의 갯수에 칸에 적혀있는 숫자를 곱한 값이다.  만약 3이 적혀있고 이어진 칸의 갯수가 5개라면 15점을 획득한다.
# 7. 이동을 주어진 k(최대 1000)번 진행하고나면 게임이 종료되고 획득한 점수를 출력한다.
def sol23288():
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 공간상의 모든 칸을 클러스터로 분류
    # 같은 클러스터에 속한 칸은 도착시 얻는 점수도 같음
    cluster = [[-1] * m for _ in range(n)]
    score_of_cluster = []
    idx = 0

    # 점수를 계산하기 위한 함수
    def score(i, j):
        nonlocal idx

        # 이미 탐색이 끝난 클러스터라면 바로 점수를 반환
        if cluster[i][j] >= 0:
            return score_of_cluster[cluster[i][j]]

        # 현재 위치를 기준으로 클러스터 분류
        num = board[i][j]
        q = [(i, j)]
        cluster[i][j] = idx
        size = 1
        while q:
            nq = []
            for cr, cc in q:
                if cr > 0:
                    nr, nc = cr - 1, cc
                    if cluster[nr][nc] == -1 and board[nr][nc] == num:
                        cluster[nr][nc] = idx
                        size += 1
                        nq.append((nr, nc))
                if cr < n - 1:
                    nr, nc = cr + 1, cc
                    if cluster[nr][nc] == -1 and board[nr][nc] == num:
                        cluster[nr][nc] = idx
                        size += 1
                        nq.append((nr, nc))
                if cc > 0:
                    nr, nc = cr, cc - 1
                    if cluster[nr][nc] == -1 and board[nr][nc] == num:
                        cluster[nr][nc] = idx
                        size += 1
                        nq.append((nr, nc))
                if cc < m - 1:
                    nr, nc = cr, cc + 1
                    if cluster[nr][nc] == -1 and board[nr][nc] == num:
                        cluster[nr][nc] = idx
                        size += 1
                        nq.append((nr, nc))
            q = nq

        # 클러스터의 획득 점수 계산 후 저장하고 클러스터 인덱스를 증가시킨 뒤 점수 반환
        res = size * num
        score_of_cluster.append(res)
        idx += 1

        return res

    # 방향
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 주사위의 상태 - 윗면, 북쪽을 바라보는 면, 동쪽을 바라보는 면
    dice = [1, 2, 3]

    # 초기 이동방향 (0: 동 / 1: 남 / 2: 서 / 3: 북)
    d = 0

    # 주사위의 위치
    r, c = 0, 0

    # 획득 점수
    answer = 0

    # k 번 이동
    for _ in range(k):
        # 이동할 방향으로 칸이 없다면 방향을 반대로 전환하여 다시이동
        nr, nc = r + directions[d][0], c + directions[d][1]
        if not (0 <= nr < n and 0 <= nc < m):
            d = (d + 2) % 4
            nr, nc = r + directions[d][0], c + directions[d][1]

        # 주사위를 이동시키고 상태를 변경
        r, c = nr, nc

        # 동쪽
        if d == 0:
            dice = 7 - dice[2], dice[1], dice[0]
        # 남쪽
        elif d == 1:
            dice = dice[1], 7 - dice[0], dice[2]
        # 서쪽
        elif d == 2:
            dice = dice[2], dice[1], 7 - dice[0]
        # 북쪽
        else:
            dice = 7 - dice[1], dice[0], dice[2]

        # 점수 획득
        answer += score(r, c)

        # 방향전환
        if 7 - dice[0] > board[r][c]:
            d = (d + 1) % 4
        elif 7 - dice[0] < board[r][c]:
            d = (d + 3) % 4

    # 총점 반환
    return answer
