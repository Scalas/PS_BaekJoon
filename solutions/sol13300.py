import sys
from math import ceil

input = sys.stdin.readline


# 13300 방 배정
# 학생들의 학년과 성별에 따라 최대 k명이 사용할 수 있는 방을 배정할 때
# 필요한 방의 최소갯수를 구하는 문제
def sol13300():
    n, k = map(int, input().split())
    room = [[0] * 6 for _ in range(2)]
    for _ in range(n):
        s, y = map(int, input().split())
        room[s][y-1] += 1

    return sum([ceil(room[i][j] / k) for i in range(2) for j in range(6)])
