import sys

input = sys.stdin.readline


# 19237 어른 상어
# n * n 공간에서 규칙에 따라 상어들이 움직일 때
# 공간에 상어가 한마리만 남을 때 까지 걸리는 시간을 구하는 문제
def sol19237():
    directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m, k = map(int, input().split())

    # 처음 공간의 상태
    space = [list(map(int, input().split())) for _ in range(n)]

    # 상어들의 초기 방향
    init_direction = list(map(int, input().split()))

    # 상어들의 번호, 위치, 방향 리스트
    q = []
    for i in range(n):
        for j in range(n):
            if space[i][j]:
                q.append([space[i][j]-1, i, j, init_direction[space[i][j] - 1]])
                space[i][j] = [k, space[i][j]-1]
            else:
                space[i][j] = [0, 0]

    # 상어의 번호순으로 오름차순 정렬
    q.sort()

    # 상어들의 방향별 우선순위
    shark = [[list(map(int, input().split())) for _ in range(4)] for _ in range(m)]

    # 상어가 한마리만 남거나 1000초를 넘기기 전까지 반복
    t = 0
    while len(q) > 1 and t <= 1000:
        mq = []
        # 상어의 이동
        for num, r, c, curd in q:
            # 각자의 우선순위 순으로 공간을 벗어나지 않고 이동가능한 좌표 탐색
            pos = []
            for d in shark[num][curd-1]:
                nr, nc = r + directions[d][0], c + directions[d][1]
                # 공간을 벗어날경우 패스
                if 0 <= nr < n and 0 <= nc < n:
                    pos.append((nr, nc, d))

            # 냄새가 없는 공간을 먼저 탐색
            moved = False
            for nr, nc, d in pos:
                # 냄새가 없는 공간이 있다면 mq에 이동후 상태를 삽입
                if not space[nr][nc][0]:
                    mq.append([num, nr, nc, d])
                    moved = True
                    break

            # 냄새가 없는 공간으로 이동햇을 경우 다음 상어로
            if moved:
                continue

            # 냄새가 없는 공간을 찾지 못했다면 자신의 냄새가 있는 공간으로 이동
            for nr, nc, d in pos:
                if space[nr][nc][0] and space[nr][nc][1] == num:
                    mq.append([num, nr, nc, d])
                    break

        # 기존 냄새의 감소
        for i in range(n):
            for j in range(n):
                if space[i][j][0]:
                    space[i][j][0] -= 1

        # 상어의 이동결과 반영
        # 번호가 작은 상어부터 반영되기 때문에 자연스레 같은칸의 번호가 더 큰 상어를 배제할 수 있다.
        nq = []
        for num, r, c, curd in mq:
            # 냄새가 없는 칸이거나 자신의 냄새가 있는 칸일 경우 냄새를 뿌린다
            if not space[r][c][0] or space[r][c][1] == num:
                space[r][c] = [k, num]
                nq.append([num, r, c, curd])

        q = nq
        t += 1

    # 1000초가 넘었다면 -1을, 그렇지 않다면 걸린 시간을 반환
    return t if t <= 1000 else -1
