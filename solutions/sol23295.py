import sys

input = sys.stdin.readline


# 23295 스터디 시간 정하기 1
# 스터디 참가자 수 n과 총 스터디 시간 t가 주어지고
# n명의 참가자가 스터디에 참여 가능한 시간대가 주어졌을 때
# 스터디 참가자들의 시간만족도의 합이 최대가 되는 스터디 시작시간과 끝시간을 구하는 문제
# 단, 시간 만족도란 각 참가자가 스터디에 참가 가능한 시간의 합을 의미하며
# 만약 시간만족도의 합이 최대가되는 시간대가 여러개라면 시작시간이 가장 빠른 것을 구한다.
def sol23295():
    n, t = map(int, input().split())

    # 참가자들의 참여가능 시간 기록
    time = [0] * 100002
    max_time = 0
    for _ in range(n):
        for _ in range(int(input())):
            u, v = map(int, input().split())
            time[u] += 1
            time[v] -= 1
            max_time = max(max_time, v)

    # 각 시간대별 참여가능한 참가자의 수를 누적합으로 구함
    for i in range(max_time - 1):
        time[i + 1] += time[i]

    # i시간까지의 참가자들의 누적 참여시간수(시간만족도의 합)를 누적합으로 구함
    for i in range(max_time - 1):
        time[i + 1] += time[i]

    # 최대 시간만족도와 그 때의 스터디 시간대
    max_sat = 0
    start, end = 0, t

    # 모든 길이 t의 구간에서의 시간만족도의 합으로 max_sat 갱신
    for s in range(max_time - t + 1):
        e = s + t
        sat = time[e - 1] - time[s - 1]
        if sat > max_sat:
            max_sat = sat
            start, end = s, e

    return f'{start} {end}'
