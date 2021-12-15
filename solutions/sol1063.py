import sys

input = sys.stdin.readline


# 1063 킹
# 체스판 위에서 킹과 돌을 주어진 명령에 따라 움직인 뒤 최종 위치를 구하는 문제
def sol1063():
    directions = {'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0), 'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)}
    r, c, n = map(lambda x:int(x) if x.isdigit() else x, input().split())

    # 체스판에서의 위치를 행렬인덱스로 변환
    kr = 8 - int(r[1])
    kc = ord(r[0]) - ord('A')
    sr = 8 - int(c[1])
    sc = ord(c[0]) - ord('A')

    for _ in range(n):
        # 명령의 방향
        cmd = input().rstrip()
        d = directions[cmd]

        # 킹이 이동할 위치
        nkr, nkc = kr + d[0], kc + d[1]

        # 킹이 보드를 벗어날 경우 건너뜀
        if not (0 <= nkr < 8 and 0 <= nkc < 8):
            continue

        # 킹이 이동할 위치에 돌이 있는 경우
        if nkr == sr and nkc == sc:
            # 돌이 이동할 위치
            nsr, nsc = sr + d[0], sc + d[1]

            # 돌이 보드를 벗어날 경우 건너뜀
            if not (0 <= nsr < 8 and 0 <= nsc < 8):
                continue

            # 돌의 이동
            sr, sc = nsr, nsc

        # 킹의 이동
        kr, kc = nkr, nkc

    # 킹과 돌의 최종위치를 체스판에서의 위치로 변환하여 반환
    return ''.join([chr(kc + ord('A')), str(8 - kr), '\n', chr(sc + ord('A')), str(8 - sr)])
