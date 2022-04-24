import sys

input = sys.stdin.readline


# 18808 스티커 붙이기
# n * m 격자형태의 공책에 k개의 스티커를 규칙에 따라 붙일 때
# 모든 스티커를 붙이고난 후 공책에 스티커가 붙어있는 칸의 갯수를 구하는 문제
# 1. 스티커는 회전하지 않은 상태로 시작하여 공책의 맨 왼쪽 위에서부터 오른쪽 아래로 내려가며 붙일 공간을 탐색
# 2. 붙일 공간이 있다면 바로 스티커를 붙이고 붙일 공간이 없을 경우 90도씩 오른쪽으로 회전하며 다시 시도
# 3. 만약 모든 경우를 탐색해도 스티커를 붙일 수 없다면 스티커를 버림
def sol18808():
    n, m, k = map(int, input().split())

    # 공책
    board = [[0] * m for _ in range(n)]

    for _ in range(k):
        row, col = map(int, input().split())
        # 스티커의 모양과 차지하는 칸 갯수
        sticker = [list(map(int, input().split())) for _ in range(row)]

        # 스티커를 회전시킨 케이스도 검사
        for _ in range(4):
            # 스티커를 붙이는데 성공했는지 여부
            done = False

            # 스티커의 시작지점 탐색
            for i in range(n-row+1):
                for j in range(m-col+1):
                    # 해당 지점에서 스티커를 붙일 수 있는지 탐색
                    check = False

                    for r in range(row):
                        for c in range(col):
                            # 한칸이라도 겹치는 경우 붙일 수 없음
                            if sticker[r][c] and board[i+r][j+c]:
                                check = True
                                break
                        if check:
                            break
                    if check:
                        continue

                    # 붙일 수 있는 경우 스티커를 붙임
                    for r in range(row):
                        for c in range(col):
                            board[i+r][j+c] += sticker[r][c]
                    done = True
                    break
                if done:
                    break
            if done:
                break

            # 스티커 회전
            sticker = rotate(sticker)
            row, col = col, row

    # 스티커가 붙어있는 칸 수 반환
    return sum(map(sum, board))


# 스티커 회전 함수
def rotate(a):
    r, c = len(a), len(a[0])
    res = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            res[j][r-i-1] = a[i][j]
    return res
