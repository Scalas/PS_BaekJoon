import sys

input = sys.stdin.readline


# 2931 가스관
# 7 종류의 가스관으로 두 장소를 이은 설계도에서 하나의 가스관이 지워진 상태가 주어졌을 때
# 지워진 가스관의 위치와 종류를 구하는 문제
# 단, 두 장소를 가스관으로 잇는 경로는 반드시 단 하나 존재하며
# 낭비되는 가스관 없이 모두 사용해야만 두 장소를 이을 수 있는 케이스만 주어진다
def sol2931():
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    up = {'|', '+', '1', '4'}
    down = {'|', '+', '2', '3'}
    right = {'-', '+', '3', '4'}
    left = {'-', '+', '1', '2'}

    n, m = map(int, input().split())
    europe = [list(input().rstrip()) for _ in range(n)]

    # M 또는 Z에서 가스관이 끊어진 곳까지 이동
    def move_to_end(row, col, dst):
        cur = europe[row][col]
        while europe[row][col] != '.':
            cur = europe[row][col]
            if dst == 0:
                if cur == '1':
                    dst = 1
                elif cur == '4':
                    dst = 3
            elif dst == 1:
                if cur == '3':
                    dst = 0
                elif cur == '4':
                    dst = 2
            elif dst == 2:
                if cur == '2':
                    dst = 1
                elif cur == '3':
                    dst = 3
            elif dst == 3:
                if cur == '1':
                    dst = 2
                elif cur == '2':
                    dst = 0
            row, col = row + direction[dst][0], col + direction[dst][1]
        return row, col

    # 가스관이 끊어진 위치에서 가스관의 종류를 알아내는 함수
    def pipe(row, col):
        u, d, r, l = 0, 0, 0, 0
        ac = 0
        if row > 0 and europe[row - 1][col] in up:
            if europe[row - 1][col] == '*':
                ac += 1
            u = 1
        if row < n - 1 and europe[row + 1][col] in down:
            if europe[row + 1][col] == '*':
                ac += 1
            d = 1
        if col > 0 and europe[row][col - 1] in left:
            if europe[row][col - 1] == '*':
                ac += 1
            l = 1
        if col < m - 1 and europe[row][col + 1] in right:
            if europe[row][col + 1] == '*':
                ac += 1
            r = 1

        total = u + d + r + l
        if total == 4:
            return '+'
        if u:
            if d:
                return '|'
            if l:
                return '3'
            if r:
                return '2'
        if d:
            if l:
                return '4'
            if r:
                return '1'

        return '-'

    # M, Z의 좌표를 알아냄
    count = 0
    mr, mc, md = 0, 0, 0
    zr, zc, zd = 0, 0, 0
    for i in range(n):
        for j in range(m):
            if europe[i][j] == '.':
                continue

            if europe[i][j] == 'M':
                europe[i][j] = '*'
                mr, mc = i, j
            elif europe[i][j] == 'Z':
                europe[i][j] = '*'
                zr, zc = i, j
            else:
                count += 1

    # 만약 파이프가 하나도 존재하지 않을 경우 두 장소는 한칸을 사이에 두고
    # 가로 또는 세로파이프로 이어져야함
    if not count:
        if mr == zr:
            return ' '.join(map(str, [mr + 1, min(mc, zc) + 2, '-']))
        if mc == zc:
            return ' '.join(map(str, [min(mr, zr) + 2, mc + 1], '|'))

    # M과 처음으로 이어지는 파이프 탐색
    if mr > 0 and europe[mr - 1][mc] in up:
        mr, mc, md = mr - 1, mc, 0
    elif mr < n - 1 and europe[mr + 1][mc] in down:
        mr, mc, md = mr + 1, mc, 2
    elif mc > 0 and europe[mr][mc - 1] in left:
        mr, mc, md = mr, mc - 1, 3
    elif mc < m - 1 and europe[mr][mc + 1] in right:
        mr, mc, md = mr, mc + 1, 1
    mr, mc = move_to_end(mr, mc, md)

    # 만약 M과 이어지는 파이프가 존재한다면 그 파이프로부터 파이프가
    # 끊어진 위치까지 이동하여 위치와 종류를 알아냄
    if europe[mr][mc] != '*':
        return ' '.join(map(str, [mr + 1, mc + 1, pipe(mr, mc)]))

    # Z와 처음으로 이어지는 파이프 탐색
    if zr > 0 and europe[zr - 1][zc] in up:
        zr, zc, zd = zr - 1, zc, 0
    elif zr < n - 1 and europe[zr + 1][zc] in down:
        zr, zc, zd = zr + 1, zc, 2
    elif zc > 0 and europe[zr][zc - 1] in left:
        zr, zc, zd = zr, zc - 1, 3
    elif zc < m - 1 and europe[zr][zc + 1] in right:
        zr, zc, zd = zr, zc + 1, 1
    zr, zc = move_to_end(zr, zc, zd)

    # 만약 Z와 이어지는 파이프가 존재한다면 그 파이프로부터 파이프가
    # 끊어진 위치까지 이동하여 위치와 종류를 알아냄
    if europe[zr][zc] != '*':
        return ' '.join(map(str, [zr + 1, zc + 1, pipe(zr, zc)]))
