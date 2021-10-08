import sys

input = sys.stdin.readline


# 2460 지능형 기차 2
# 10개의 역이 있고 각 역마다 내리는 사람과 타는 사람이 주어졌을 때
# 기차안에 가장 많은 사람이 남아있을 때의 사람 수를 구하는 문제
def sol2460():
    res = 0
    cur = 0
    for _ in range(10):
        o, i = map(int, input().split())
        cur = cur + i - o
        res = max(res, cur)
    return res
