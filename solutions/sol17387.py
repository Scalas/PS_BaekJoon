import sys

input = sys.stdin.read


# 17387 선분 교차 2
# 선분 교차 1 과 같은 문제이지만 세 개 이상의 점이 일직선상에 존재할 수 있음
# 마찬가지로 CCW 응용문제이며 선분 교차 1 의 코드에 약간의 조건을 추가하는 것으로 해결 가능
def sol17387():
    # 선분을 이루는 네 점
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    p1, p2, p3, p4 = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

    # 각 선분을 기준으로 한 CCW 값의 곱
    v1, v2 = ccw(p1, p2, p3) * ccw(p1, p2, p4), ccw(p3, p4, p1) * ccw(p3, p4, p2)

    # v1, v2 중 하나라도 0보다 클 경우 선분은 교차하지 않음
    if v1 > 0 or v2 > 0:
        return 0

    # 셋 이상의 점이 일직선상에 있는 경우
    elif v1 == v2 == 0:
        # p1 <= p2 , p3 <= p4 가 되도록 함
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3

        # 세 점이 일직선상에 있지만 선분 l2의 점 중 l1에 가장 가까운 점이 l1과 떨어져있어 교차하지 않는 경우를 제외하면
        # 두 선분은 교차한다.
        return 0 if p2 < p3 or p4 < p1 else 1

    # 그 외의 경우 두 선분은 교차함
    else:
        return 1


# CCW 함수
def ccw(p1, p2, p3):
    res = (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])
    return 1 if res > 0 else (-1 if res < 0 else 0)
