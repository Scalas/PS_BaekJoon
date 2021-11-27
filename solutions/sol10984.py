import sys
from math import ceil

input = sys.stdin.readline


# 10984 내 학점을 구해줘
# 학기별 학점과 평점을 구하는 문제
def sol10984():
    answer = []
    for _ in range(int(input())):
        n = int(input())
        score, time = 0, 0
        for _ in range(n):
            c, g = map(float, input().split())
            score += c * g
            time += c
        answer.append(' '.join(map(str, [int(time), round(score / time, 1)])))
    return '\n'.join(answer)
