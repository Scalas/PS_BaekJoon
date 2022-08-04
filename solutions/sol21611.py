import sys

input = sys.stdin.readline


# 21611 마법사 상어와 블리자드
# n * n 격자공간의 중앙에 상어가 있고 (n은 홀수)
# 다음 행동을 반복했을 때, 폭발한 1번구슬의 갯수 + 폭발한 2번 구슬의 갯수 * 2 +
# 폭발한 3번 구슬의 갯수 * 3을 구하는 문제

# 1. 상어의 블리자드
#   상어는 상하좌우로 거리를 조절해가며 블리자드를 사용하여
#   사용한 방향으로 거리만큼의 구슬을 파괴한다
#
# 2. 구슬의 이동
#   이 때, 상어에 의해 구슬이 파괴되면 구슬은 빈자리를 메꾸며
#   바깥에서부터 안쪽으로 시계방향으로 회전하며 이동한다
#
# 3. 구슬의 폭발/이동
#   이동 후 회전하는(소용돌이)순서대로 연속한 4개이상의 같은 종류의 구슬은 폭발하고
#   폭발한 자리를 다시 구슬이 이동하여 메꾸며 이를 더이상 폭발이 일어나지 않을 때 까지 반복한다
#
# 4. 구슬의 변화
#   더이상 폭발이 일어나지 않으면 연속한 구슬의 그룹은 (연속한 구슬의 갯수), (구슬의 종류)를 값으로 하는
#   두 개의 구슬로 변화한다
def sol21611():
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 상어의 위치
    sr = sc = (n - 1) // 2

    # 각 좌표의 인덱스를 구하고 구슬을 리스트에 삽입
    pos_index = [[0] * n for _ in range(n)]
    r, c = sr, sc
    gap = 1
    d = 0
    idx = 0
    marbles = []
    for _ in range(n - 1):
        # 좌측/하단 이동
        if not d:
            for i in range(1, gap + 1):
                c -= 1
                pos_index[r][c] = idx
                marbles.append(board[r][c])
                idx += 1
            for i in range(1, gap + 1):
                r += 1
                pos_index[r][c] = idx
                marbles.append(board[r][c])
                idx += 1
            d = 1

        # 우측/상단 이동
        else:
            for i in range(1, gap + 1):
                c += 1
                pos_index[r][c] = idx
                marbles.append(board[r][c])
                idx += 1
            for i in range(1, gap + 1):
                r -= 1
                pos_index[r][c] = idx
                marbles.append(board[r][c])
                idx += 1
            d = 0
        gap += 1

    # 좌측으로 마지막 한번 이동
    for i in range(1, gap):
        c -= 1
        pos_index[r][c] = idx
        marbles.append(board[r][c])
        idx += 1

    bursted = [0] * 3

    # 구슬 폭발
    def burst(marbles):
        res = []
        cnt = 0
        for num in marbles:
            if res and res[-1] == num:
                cnt += 1
                res.append(num)
            else:
                if cnt >= 4:
                    for _ in range(cnt):
                        bursted[res.pop() - 1] += 1
                cnt = 1
                res.append(num)
        if cnt >= 4:
            for _ in range(cnt):
                bursted[res.pop() - 1] += 1
        return res

    # 구슬 변화
    def change(marbles):
        if not marbles:
            return marbles
        res = []
        pre = marbles[0]
        cnt = 1
        for i in range(1, len(marbles)):
            num = marbles[i]
            if pre == num:
                cnt += 1
            else:
                res.append(cnt)
                res.append(pre)
                cnt = 1
                pre = num
        if cnt:
            res.append(cnt)
            res.append(pre)
        return res if len(res) < n ** 2 else res[:n ** 2 - 1]

    # m 번의 블리자드
    for _ in range(m):
        # 구슬 파괴
        d, s = map(int, input().split())
        r, c = sr, sc
        for _ in range(s):
            r += direction[d - 1][0]
            c += direction[d - 1][1]
            idx = pos_index[r][c]
            if idx < len(marbles):
                marbles[idx] = 0

        # 구슬의 이동
        marbles = [num for num in marbles if num]

        # 더이상 폭발이 발생하지 않을 때 까지 폭발과 이동 반복
        while True:
            nxt = burst(marbles)
            if len(marbles) == len(nxt):
                break
            marbles = nxt

        # 구슬 그룹이 두개로 변화
        marbles = change(marbles)

    return bursted[0] + bursted[1] * 2 + bursted[2] * 3

