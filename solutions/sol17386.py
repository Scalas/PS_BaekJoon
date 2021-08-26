import sys

input = sys.stdin.read


# 17387 선분 교차 1
# 두 선분의 시작점, 끝점의 좌표가 주어졌을 때 두 선분의 교차여부를 구하는 문제
# CCW 응용문제이다.
def sol17387():
    # 네 점의 좌표
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    p1, p2, p3, p4 = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

    # 선분 p1-p2 와 p3-p4를 각각 기준으로 한 CCW값의 곱
    v1, v2 = ccw(p1, p2, p3) * ccw(p1, p2, p4), ccw(p3, p4, p1) * ccw(p3, p4, p2)

    # 두 값중 하나라도 0보다 크다면 두 선분은 교차하지 않는다.
    if v1 > 0 or v2 > 0:
        return 0

    # 그 외의 경우 두 선분은 교차한다.
    return 1


# CCW 함수
def ccw(p1, p2, p3):
    res = (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])
    return 1 if res > 0 else (-1 if res < 0 else 0)
