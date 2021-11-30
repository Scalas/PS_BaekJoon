import sys

input = sys.stdin.readline


# 17779 게리맨더링 2
# n * n 격자형 지도에서 경계선을 기준으로 선거구역을 5개로 분할
# x, y, d1, d2가 주어졌을 때
# 경계선의 맨 위 좌표는 (x, y)
# 맨 아래 좌표는 (x+d1+d2, y+d2-d1)
# 맨 왼쪽 좌표는 (x+d1, y-d1)
# 맨 오른쪽 좌표는 (x+d2, y+d2) 가 된다
# 이 경계선내부는 5구역, 좌상단은 1구역, 우상단은 2구역, 좌하단은 3구역, 우하단은 4구역이라 한다
# 인구수 총합이 가장 많은 곳과 가장 적은 곳의 차가 최소가 되는 경우를 구하는 문제
def sol17779():
    n = int(input())
    # 각 라인의 누적합을 구하여 구간합을 O(1)로 구하기 위한 전처리를 한다
    board = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n-1):
            board[i][j+1] += board[i][j]

    answer = 10 ** 9

    # x는 0부터 시작하여 경계선의 최소 높이가 3이기 때문에 n-3까지 가능
    for x in range(n-2):
        # y가 좌우에 딱붙으면 경계선을 그을 수없기 때문에 1부터 시작하여 n-2까지 가능
        for y in range(1, n-1):
            # y - d1 >= 0 이므로 d1 <= y
            for d1 in range(1, y+1):
                # y + d2 < n 이므로 d2 < n - y
                # x + d1 + d2 < n 이므로 d2 < n - x - d1
                for d2 in range(1, min(n-y, n-x-d1)):
                    # 맨 위, 맨 아래, 맨 왼쪽, 맨 오른쪽의 좌표
                    tx, ty = x, y
                    bx, by = x+d1+d2, y+d2-d1
                    lx, ly = x+d1, y-d1
                    rx, ry = x+d2, y+d2

                    # 각 구역의 인구수 총합
                    a = [0] * 5

                    # 각 행에 대해
                    for r in range(n):
                        # 경계선 위쪽인 경우
                        # 행의 ty 번째 열까지는 1구역의 인구
                        # ty+1 부터 마지막까지는 2구역의 인구
                        if r < tx:
                            a[0] += board[r][ty]
                            a[1] += board[r][-1] - board[r][ty]

                        # 경계선 아래쪽인 경우
                        # 행의 by-1 번째 열까지는 3구역의 인구
                        # by 부터 마지막까지는 4구역의 인구
                        elif r > bx:
                            a[2] += board[r][by-1]
                            a[3] += board[r][-1] - board[r][by-1]

                        # 경계선이 존재하는 행인 경우
                        else:
                            # 경계선 시작높이를 기준으로한 행수
                            diff = r - x

                            # 경계선의 좌, 우 인덱스
                            left, right = ty-diff, ty+diff

                            # 좌측 경계선이 맨 왼쪽을 넘어갈 경우 반대방향으로 전환
                            # 행의 left-1 까지는 3구역의 인구
                            if diff >= d1:
                                left = ly + diff - d1
                                if left:
                                    a[2] += board[r][left-1]

                            # 경계선이 맨 왼쪽을 넘어가지 않을 경우
                            # 행의 left-1 까지는 1구역의 인구
                            else:
                                a[0] += board[r][left-1]

                            # 우측 경계선이 맨 오른쪽을 넘어갈 경우 반대방향으로 전환
                            # 행의 right+1 부터 마지막까지는 4구역의 인구
                            if diff > d2:
                                right = ry + d2 - diff
                                a[3] += board[r][-1] - board[r][right]

                            # 경계선이 맨 오른쪽을 넘어가지 않을 경우
                            # 행의 right+1 부터 마지막까지는 2구역의 인구
                            else:
                                a[1] += board[r][-1] - board[r][right]

                            # 경계선 내부는 5구역의 인구
                            a[4] += (board[r][right] - (board[r][left-1] if left else 0))

                    # 최대인구수 - 최소인구수로 answer 값을 갱신
                    answer = min(answer, max(a) - min(a))

    # 최대인구수와 최소인구수의 차의 최솟값 반환
    return answer
