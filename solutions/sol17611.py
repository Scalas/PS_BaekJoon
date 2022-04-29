import sys
from collections import defaultdict

input = sys.stdin.readline


# 17611 직각다각형
# x축, y축에 수평인 선분들로만 이루어진 직각다각형의 꼭짓점 n개가 주어졌을 때
# 적절한 수평 혹은 수직 직선 하나를 그어 나올 수 있는 직각다각형과의 교점의 개수의 최댓값을 구하는 문제
def sol17611():
    n = int(input())
    h = defaultdict(int)
    v = defaultdict(int)

    # 꼭짓점의 좌표
    pos = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        # 이전 꼭짓점과 현재 꼭짓점
        px, py = pos[i-1]
        cx, cy = pos[i]

        # x, y값을 px < cx,  py < cy 가 되도록 함
        if cx < px:
            cx, px = px, cx
        if cy < py:
            cy, py = py, cy

        # 수평선인 경우 수평선 배열에 표시
        if py == cy:
            h[px] += 1
            h[cx] -= 1

        # 수직선인 경우 수직선 배열에 표시
        else:
            v[py] += 1
            v[cy] -= 1

    # 교점의 최대갯수
    answer = 0

    # 수직, 수평선 배열의 누적합의 최댓값이 교점의 최대갯수가 된다
    acc = 0
    for i, val in sorted(h.items()):
        acc += val
        answer = max(answer, acc)
    for i, val in sorted(v.items()):
        acc += val
        answer = max(answer, acc)

    return answer
