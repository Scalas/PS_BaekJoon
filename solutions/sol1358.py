import sys

input = sys.stdin.readline


# 1358 하키
# 하키장의 기준점 x, y 와 중간 직사각형 구간의 너비와 높이 w, h가 주어지고
# 양쪽에 붙어있는 반원의 지름이 h 라고 할 때
# 주어지는 좌표들중 하키장 내부에 있는 점의 갯수를 구하는 문제
def sol1358():
    w, h, x, y, p = map(int, input().split())
    r = h // 2
    rsq = r ** 2

    def is_in_link(px, py):
        if py < y:
            return 0
        if py > y + h:
            return 0
        if px < x - r:
            return 0
        if px > x + w + r:
            return 0
        if x <= px <= x + w:
            return 1
        if (px - x) ** 2 + (py - y - r) ** 2 <= rsq:
            return 1
        if (px - x - w) ** 2 + (py - y - r) ** 2 <= rsq:
            return 1
        return 0

    return sum([is_in_link(*map(int, input().split())) for _ in range(p)])
