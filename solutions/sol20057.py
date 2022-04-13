import sys
from math import floor

input = sys.stdin.readline


def sol20057():
    # 격자의 크기
    n = int(input())

    # 격자의 상태
    board = [list(map(int, input().split())) for _ in range(n)]

    # 방향 (좌, 하, 우, 상)
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # 토네이도 시작위치
    tr, tc = n // 2, n // 2

    # 토네이도 이동거리
    distance = 1

    # 토네이도 방향
    d = 0

    # 격자 밖으로 나간 모래의 양
    answer = 0

    # 토네이도가 모래를 날린 후의 상태를 반영
    def blow(tr, tc, dir):
        nonlocal answer

        # 토네이도가 이동한 자리의 모래의 양
        dust = board[tr][tc]

        # 모래의 1%, 2%, 5%, 7%, 10%, 모두 날리고나서 남은 나머지
        p1 = floor(dust * 0.01)
        p2 = floor(dust * 0.02)
        p5 = floor(dust * 0.05)
        p7 = floor(dust * 0.07)
        p10 = floor(dust * 0.1)
        remain = dust - p1 * 2 - p2 * 2 - p7 * 2 - p10 * 2 - p5

        # 토네이도의 방향이 왼쪽일 경우
        if dir == 0:
            if tr > 0:
                board[tr-1][tc] += p7
            else:
                answer += p7

            if tr < n-1:
                board[tr+1][tc] += p7
            else:
                answer += p7

            if tr > 1:
                board[tr-2][tc] += p2
            else:
                answer += p2

            if tr < n-2:
                board[tr+2][tc] += p2
            else:
                answer += p2

            if tr > 0 and tc > 0:
                board[tr-1][tc-1] += p10
            else:
                answer += p10

            if tr < n-1 and tc > 0:
                board[tr+1][tc-1] += p10
            else:
                answer += p10

            if tr > 0 and tc < n-1:
                board[tr-1][tc+1] += p1
            else:
                answer += p1

            if tr < n-1 and tc < n-1:
                board[tr+1][tc+1] += p1
            else:
                answer += p1

            if tc > 1:
                board[tr][tc-2] += p5
            else:
                answer += p5

            if tc > 0:
                board[tr][tc-1] += remain
            else:
                answer += remain

        # 토네이도의 방향이 아래쪽일 경우
        elif dir == 1:
            if tc > 0:
                board[tr][tc-1] += p7
            else:
                answer += p7

            if tc < n-1:
                board[tr][tc+1] += p7
            else:
                answer += p7

            if tc > 1:
                board[tr][tc-2] += p2
            else:
                answer += p2

            if tc < n-2:
                board[tr][tc+2] += p2
            else:
                answer += p2

            if tr < n-1 and tc > 0:
                board[tr+1][tc-1] += p10
            else:
                answer += p10

            if tr < n-1 and tc < n-1:
                board[tr+1][tc+1] += p10
            else:
                answer += p10

            if tr > 0 and tc > 0:
                board[tr-1][tc-1] += p1
            else:
                answer += p1

            if tr > 0 and tc < n-1:
                board[tr-1][tc+1] += p1
            else:
                answer += p1

            if tr < n-2:
                board[tr+2][tc] += p5
            else:
                answer += p5

            if tr < n-1:
                board[tr+1][tc] += remain
            else:
                answer += remain

        # 토네이도의 방향이 오른쪽일 경우
        elif dir == 2:
            if tr > 0:
                board[tr-1][tc] += p7
            else:
                answer += p7

            if tr < n-1:
                board[tr+1][tc] += p7
            else:
                answer += p7

            if tr > 1:
                board[tr-2][tc] += p2
            else:
                answer += p2

            if tr < n-2:
                board[tr+2][tc] += p2
            else:
                answer += p2

            if tr > 0 and tc < n-1:
                board[tr-1][tc+1] += p10
            else:
                answer += p10

            if tr < n-1 and tc < n-1:
                board[tr+1][tc+1] += p10
            else:
                answer += p10

            if tr > 0 and tc > 0:
                board[tr-1][tc-1] += p1
            else:
                answer += p1

            if tr < n-1 and tc > 0:
                board[tr+1][tc-1] += p1
            else:
                answer += p1

            if tc < n-2:
                board[tr][tc+2] += p5
            else:
                answer += p5

            if tc < n-1:
                board[tr][tc+1] += remain
            else:
                answer += remain

        # 토네이도의 방향이 위쪽일 경우
        elif dir == 3:
            if tc > 0:
                board[tr][tc-1] += p7
            else:
                answer += p7

            if tc < n-1:
                board[tr][tc+1] += p7
            else:
                answer += p7

            if tc > 1:
                board[tr][tc-2] += p2
            else:
                answer += p2

            if tc < n-2:
                board[tr][tc+2] += p2
            else:
                answer += p2

            if tr > 0 and tc > 0:
                board[tr-1][tc-1] += p10
            else:
                answer += p10

            if tr > 0 and tc < n-1:
                board[tr-1][tc+1] += p10
            else:
                answer += p10

            if tr < n-1 and tc > 0:
                board[tr+1][tc-1] += p1
            else:
                answer += p1

            if tr < n-1 and tc < n-1:
                board[tr+1][tc+1] += p1
            else:
                answer += p1

            if tr > 1:
                board[tr-2][tc] += p5
            else:
                answer += p5

            if tr > 0:
                board[tr-1][tc] += remain
            else:
                answer += remain

    # 같은거리로 좌 하 또는 우 상으로 두번 이동한 후 거리 + 1
    # 이렇게 n-1 번 반복하면 (0, n-1) 에 도달
    # 이동하면서 매순간 blow를 실행
    for _ in range(n-1):
        # 이동 1
        dr, dc = direction[d]
        for _ in range(distance):
            tr, tc = tr + dr, tc + dc
            blow(tr, tc, d)

        # 방향전환
        d = (d + 1) % 4

        # 이동 2
        dr, dc = direction[d]
        for _ in range(distance):
            tr, tc = tr + dr, tc + dc
            blow(tr, tc, d)

        # 방향전환
        d = (d + 1) % 4

        # 이동거리 증가
        distance += 1

    # (0, n-1)에서 (0, 0)으로 이동
    dr, dc = direction[d]
    for _ in range(distance-1):
        tr, tc = tr + dr, tc + dc
        blow(tr, tc, d)

    return answer
