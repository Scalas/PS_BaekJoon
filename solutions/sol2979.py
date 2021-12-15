import sys

input = sys.stdin.readline


# 2979 트럭 주차
# 트럭이 1대, 2대, 3대일때의 주차장의 요금과 세 대의 트럭의 주차장 진입시간, 퇴출시간이 주어졌을 때
# 총 요금을 구하는 문제
def sol2979():
    fee = [0, *map(int, input().split())]
    fee[2] *= 2
    fee[3] *= 3

    state = [0] * 101
    s, e = 100, 0
    for _ in range(3):
        i, o = map(int, input().split())
        s = min(s, i)
        e = max(e, o)
        state[i] += 1
        state[o] -= 1
    for i in range(s, e):
        state[i+1] += state[i]

    return sum([fee[state[i]] for i in range(s, e)])
