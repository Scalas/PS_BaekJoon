import sys

input = sys.stdin.readline


# 2578 빙고
# 3줄의 빙고를 완성하는 시점을 구하는 문제
def sol2578():
    d = {}
    for i in range(5):
        line = list(map(int, input().split()))
        for j in range(5):
            d[line[j]] = (i, j, )

    bingo = [0] * 12
    nums = [*map(int, sys.stdin.read().split())]
    cnt = 0
    for i in range(25):
        r, c = d[nums[i]]
        bingo[r] += 1
        if bingo[r] == 5:
            cnt += 1
        bingo[c+5] += 1
        if bingo[c+5] == 5:
            cnt += 1
        if r == c:
            bingo[-2] += 1
            if bingo[-2] == 5:
                cnt += 1
        if r + c == 4:
            bingo[-1] += 1
            if bingo[-1] == 5:
                cnt += 1
        if cnt >= 3:
            return i+1
