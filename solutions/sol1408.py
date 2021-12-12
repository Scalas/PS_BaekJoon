import sys

input = sys.stdin.readline


# 1408 24
# 현재시간과 임무 시작시간이 주어졌을 때
# 임무 시작시간으로부터 24시간째가 되기까지 남은 시간을 구하는 문제
def sol1408():
    s, c = 0, 0
    time = list(map(int, input().split(':')))
    s = time[0] * 3600 + time[1] * 60 + time[2]
    time = list(map(int, input().split(':')))
    c = time[0] * 3600 + time[1] * 60 + time[2]

    time = 24 * 3600 - (s - c) if s > c else c - s
    h = time // 3600
    time %= 3600
    m = time // 60
    s = time % 60
    return '%02d:%02d:%02d' % (h, m, s)
