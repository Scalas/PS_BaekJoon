import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 17143 낚시왕
# 매 초마다 낚시왕은 열방향으로 1칸씩이동하여 해당 열에서 가장 땅에 가까운 상어를 잡고 맨 오른쪽칸에가면 낚시가 종료된다.
# 그 후에 상어들은 각자 정해진 방향과 속도대로 이동한다. 상어는 더이상 이동할 수 없을 경우 방향을 틀어 남은 이동횟수만큼 이동하기를 반복한다.
# 이 때, 낚시왕이 잡은 상어의 크기의 합을 구하는 문제


# 첫 번째 시도
# heapq 를 사용
def sol17143():
    r, c, m = map(int, input().split())
    # 각 열에 있는 상어들의 리스트
    ground = [[] for _ in range(c+1)]

    # 상어의 정보를 상어가 속한 열(sc) 의 리스트에
    # turn, 행, -크기, 속도, 방향으로 이루어진 리스트의 형태로 heappush
    # turn, 행, 크기 순으로 정렬의 기준이된다
    # 크기는 마이너스 값으로 넣었기 때문에 큰 순으로 정렬된다
    for _ in range(m):
        sr, sc, s, d, z = map(int, input().split())
        heappush(ground[sc], [1, sr, -z, s, d])

    answer = 0
    # 1. 낚시꾼의 이동
    for turn in range(1, c+1):
        # 2. 낚시꾼이 이동한 위치에서 가장 땅에 가까운 상어를 잡는다
        # 현재 열에 상어가 존재할 경우
        if ground[turn]:
            # 땅에 가장 가까운 상어를 잡는다
            shark = heappop(ground[turn])

            # 잡은 상어의 크기의 합을 갱신
            answer -= shark[2]

            # 같은 위치에 있는 더 작은 상어들은 잡아먹혔기 때문에 제거한다
            while ground[turn] and ground[turn][0][1] == shark[1]:
                heappop(ground[turn])

        # 3. 상어들의 이동
        for col in range(1, c+1):
            # turn 으로 이미 이동을 마친 상어를 구분하며 상어를 이동시킨다
            # 이전에 이동시킨 상어의 행 수(r)
            pre = 0
            while ground[col] and ground[col][0][0] == turn:
                shark = heappop(ground[col])
                # 이미 같은 위치에 있던 상어가 존재할 경우
                # 이 상어는 잡아먹힌 상어이기 때문에 이동시키지 않고 넘어간다
                if shark[1] == pre:
                    continue

                # 이동시킨 상어의 행 수를 갱신
                pre = shark[1]

                # 상어의 행, 열, 속도, 방향
                sr, sc, speed, direction = shark[1], col, shark[3], shark[4]

                # 상하로 이동할 경우
                if direction <= 2:
                    # 위쪽을 보고있는 경우 속도만큼 위로 이동
                    if direction == 1:
                        sr -= speed
                    # 아래쪽을 보고있는 경우 속도만큼 아래로 이동
                    else:
                        sr += speed

                    # 공통부분 - 방향을 바꾸며 이동
                    while True:
                        # 범위를 위로 벗어난 경우
                        # 방향을 아래로 바꾸고 재이동
                        if sr <= 0:
                            sr = 2 - sr
                            direction = 2

                        # 범위를 아래로 벗어난 경우
                        # 방향을 위로 바꾸고 재이동
                        elif sr > r:
                            sr = 2 * r - sr
                            direction = 1

                        # 범위안에 안착한 경우 이동 종료
                        else:
                            break

                # 좌우로 이동할 경우
                else:
                    # 오른쪽을 보고있는 경우 속도만큼 오른쪽으로 이동
                    if direction == 3:
                        sc += speed
                    # 왼쪽을 보고있는 경우 속도만큼 왼쪽으로 이동
                    else:
                        sc -= speed

                    # 공통부분 - 방향을 바꾸며 이동
                    while True:
                        # 범위를 왼쪽으로 벗어난 경우
                        # 방향을 오른쪽으로 바꾸고 재이동
                        if sc <= 0:
                            sc = 2 - sc
                            direction = 3

                        # 범위를 오른쪽으로 벗어난 경우
                        # 방향을 왼쪽으로 바꾸고 재이동
                        elif sc > c:
                            sc = 2 * c - sc
                            direction = 4

                        # 범위안에 안착한 경우 이동 종료
                        else:
                            break

                # 상어의 행과 방향의 변화를 반영한 뒤 turn 을 1 늘려 해당하는 열에 삽입
                shark[1] = sr
                shark[4] = direction
                shark[0] += 1
                heappush(ground[sc], shark)
    return answer


# 2차시도 - 첫 번째 풀이의 최적화
# 상어의 이동과정을 최적화하기 위해 상어의 속도에서 같은 구간을 반복하는 만큼을 빼준다.
def sol17143_2():
    r, c, m = map(int, input().split())
    # 각 열에 있는 상어들의 리스트
    ground = [[] for _ in range(c+1)]

    # 상어의 정보를 상어가 속한 열(c) 의 리스트에
    # turn, 행, -크기, 속도, 방향으로 이루어진 리스트의 형태로 heappush
    # turn, 행, 크기 순으로 정렬의 기준이된다
    # 크기는 마이너스 값으로 넣었기 때문에 큰 순으로 정렬된다
    for _ in range(m):
        sr, sc, s, d, z = map(int, input().split())
        # 길이 4의 칸 내에서 제자리/같은방향인 상태로 돌아오는데에 2 * (길이-1) 만큼의 이동이 필요
        # 그 배수만큼의 속도는 의미가 없기 때문에 나머지연산으로 속도를 줄여준다.
        if d <= 2:
            s %= (2 * (r-1))
        else:
            s %= (2 * (c-1))
        heappush(ground[sc], [1, sr, -z, s, d])

    answer = 0
    # 1. 낚시꾼의 이동
    for turn in range(1, c+1):
        # 2. 낚시꾼이 이동한 위치에서 가장 땅에 가까운 상어를 잡는다
        # 현재 열에 상어가 존재할 경우
        if ground[turn]:
            # 땅에 가장 가까운 상어를 잡는다
            shark = heappop(ground[turn])

            # 잡은 상어의 크기의 합을 갱신
            answer -= shark[2]

            # 같은 위치에 있는 더 작은 상어들은 잡아먹혔기 때문에 제거한다
            while ground[turn] and ground[turn][0][1] == shark[1]:
                heappop(ground[turn])

        # 3. 상어들의 이동
        for col in range(1, c+1):
            # turn 으로 이미 이동을 마친 상어를 구분하며 상어를 이동시킨다
            # 이전에 이동시킨 상어의 행 수(r)
            pre = 0
            while ground[col] and ground[col][0][0] == turn:
                shark = heappop(ground[col])
                # 이미 같은 위치에 있던 상어가 존재할 경우
                # 이 상어는 잡아먹힌 상어이기 때문에 이동시키지 않고 넘어간다
                if shark[1] == pre:
                    continue

                # 이동시킨 상어의 행 수를 갱신
                pre = shark[1]

                # 상어의 행, 열, 속도, 방향
                sr, sc, speed, direction = shark[1], col, shark[3], shark[4]

                # 상하로 이동할 경우
                if direction <= 2:
                    # 위쪽을 보고있는 경우 속도만큼 위로 이동
                    if direction == 1:
                        sr -= speed
                    # 아래쪽을 보고있는 경우 속도만큼 아래로 이동
                    else:
                        sr += speed

                    # 공통부분 - 방향을 바꾸며 이동
                    while True:
                        # 범위를 위로 벗어난 경우
                        # 방향을 아래로 바꾸고 재이동
                        if sr <= 0:
                            sr = 2 - sr
                            direction = 2

                        # 범위를 아래로 벗어난 경우
                        # 방향을 위로 바꾸고 재이동
                        elif sr > r:
                            sr = 2 * r - sr
                            direction = 1

                        # 범위안에 안착한 경우 이동 종료
                        else:
                            break

                # 좌우로 이동할 경우
                else:
                    # 오른쪽을 보고있는 경우 속도만큼 오른쪽으로 이동
                    if direction == 3:
                        sc += speed
                    # 왼쪽을 보고있는 경우 속도만큼 왼쪽으로 이동
                    else:
                        sc -= speed

                    # 공통부분 - 방향을 바꾸며 이동
                    while True:
                        # 범위를 왼쪽으로 벗어난 경우
                        # 방향을 오른쪽으로 바꾸고 재이동
                        if sc <= 0:
                            sc = 2 - sc
                            direction = 3

                        # 범위를 오른쪽으로 벗어난 경우
                        # 방향을 왼쪽으로 바꾸고 재이동
                        elif sc > c:
                            sc = 2 * c - sc
                            direction = 4

                        # 범위안에 안착한 경우 이동 종료
                        else:
                            break

                # 상어의 행과 방향의 변화를 반영한 뒤 turn을 1 늘려 해당하는 열에 삽입
                shark[1] = sr
                shark[4] = direction
                shark[0] += 1
                heappush(ground[sc], shark)
    return answer
