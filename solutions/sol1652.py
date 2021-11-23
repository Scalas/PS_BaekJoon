import sys

input = sys.stdin.readline


# 1652 누울 자리를 찾아라
# 가로, 세로의 2칸 이상의 연속하는 빈칸의 갯수를 구하는 문제
def sol1652():
    n = int(input())
    h, v = 0, 0
    pre = [0] * (n)

    for i in range(n):
        cur = list(input().rstrip())
        s = 0
        for j in range(n):
            if cur[j] == 'X':
                if j - s >= 2:
                    h += 1
                s = j + 1

                if pre[j] >= 2:
                    v += 1
                pre[j] = 0
            else:
                pre[j] += 1
        if n-s >= 2:
            h += 1
    for num in pre:
        if num >= 2:
            v += 1
    return '%d %d' % (h, v)
