import sys

input = sys.stdin.read
INF = float('inf')


# 20149 선분 교차 3
# 선분 교차 2 문제와 같지만 교점의 좌표도 구해야하는 문제
def sol20149():
    # 두 선분을 이루는 네 점의 좌표
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    p1, p2, p3, p4 = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

    # CCW 값의 곱
    v1, v2 = ccw(p1, p2, p3) * ccw(p1, p2, p4), ccw(p3, p4, p1) * ccw(p3, p4, p2)

    # 두 선분의 기울기
    try:
        a1 = (y2 - y1) / (x2 - x1)
    except:
        a1 = INF

    try:
        a2 = (y4 - y3) / (x4 - x3)
    except:
        a2 = INF

    # v1, v2 둘 중 하나라도 0 보다 크다면 두 선분은 교차하지 않음
    if v1 > 0 or v2 > 0:
        return 0

    # 셋 이상의 점이 일직선상에 존재하는 경우
    elif v1 == v2 == 0:
        # p1 <= p2 , p3 <= p4 가 되도록 한다
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3

        # 선분 l2의 점 중 선분 l1에 가장 가까운 점이 l1과 떨어져있는 경우
        # 두 선분은 교차하지 않음
        if p2 < p3 or p4 < p1:
            return 0

        # 그 외의 경우
        else:
            # 두 선분의 기울기가 같고 선분의 끝부분에서 만나는 경우
            if a1 == a2:
                if p2 == p3:
                    return '\n'.join(['1', ' '.join(map(str, p2))])
                if p1 == p4:
                    return '\n'.join(['1', ' '.join(map(str, p1))])
                return 1
            # 두 선분의 기울기가 다르고 선분의 끝부분에서 만나는 경우
            # 또는 한 선분의 길이가 0인 경우(시작과 끝점이 같은 경우)
            else:
                p = p1 if p1 == p2 or p1 == p3 or p1 == p4 else p2 if p2 == p3 or p2 == p4 else p3 if p3 == p4 else p4
                return '\n'.join(['1', ' '.join(map(str, p))])

    # 반드시 한 점에서 교차하는 경우
    else:
        # 두 선분의 기울기가 무한이 아닐 경우 일차방정식 그래프의 교점을 찾는 방식으로
        # 교점을 구한다.
        if a1 != INF and a2 != INF:
            k1 = -a1 * x1 + y1
            k2 = -a2 * x3 + y3
            resx = (k2 - k1) / (a1 - a2)
            if int(resx) == resx:
                resx = int(resx)
            resy = a1 * resx + k1
            if int(resy) == resy:
                resy = int(resy)
            return '\n'.join(['1', f'{resx} {resy}'])

        # 두 선분중 어느 하나의 기울기가 무한인 경우 교점 탐색
        else:
            if a1 == INF:
                resx = x1
                resy = a2 * resx - a2 * x3 + y3
            else:
                resx = x3
                resy = a1 * resx - a1 * x1 + y1

            if int(resx) == resx:
                resx = int(resx)
            if int(resy) == resy:
                resy = int(resy)
            return '\n'.join(['1', f'{resx} {resy}'])


# CCW 함수
def ccw(a, b, c):
    res = (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1])
    return 1 if res > 0 else -1 if res < 0 else 0
