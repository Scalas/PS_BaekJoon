import sys
from collections import defaultdict

input = sys.stdin.readline


# 2672 여러 직사각형의 전체 면적 구하기
# n개의 직사각형의 왼쪽 아래 x, y 좌표와 너비, 높이가 주어졌을 때
# 직사각형 전체가 차지하는 넓이를 구하는 문제
def sol2672():
    n = int(input())

    # 직사각형의 아래쪽 y좌표, 위쪽 y좌표, 왼쪽 x좌표, 오른쪽 x좌표 순으로 리스트에 삽입
    # 직사각형의 왼쪽, 오른쪽 x좌표를 모두 x좌표 집합에 삽입
    square = []
    pos = set()
    for i in range(n):
        x, y, w, h = map(float, input().split())
        square.append((y, y+h, x, x+w))
        pos.add(x)
        pos.add(x+w)

    # 사각형 좌표리스트와 x좌표 집합을 모두 정렬
    square.sort()
    pos = sorted(pos)

    answer = 0.0
    for i in range(1, len(pos)):
        # 이전 x좌표부터 현재 x좌표까지 존재하는 사각형의 높이의 합을 구함
        cx = pos[i]
        px = pos[i-1]
        height = 0.0
        width = cx - px
        low, high = 0, 0
        for l, h, s, e in square:
            if s > px or e < cx:
                continue
            if l <= high:
                high = max(high, h)
            else:
                height += (high - low)
                low, high = l, h

        # 마지막 구간의 높이 합산
        height += (high - low)

        # 만약 높이나 너비의 값이 정수라면 정수로 변환
        if height == int(height):
            height = int(height)
        if width == int(width):
            width = int(width)

        # 높이 * 너비로 이전 x좌표부터 현재 x좌표까지의 직사각형이 차지하는 넓이를 구하여 합산
        answer += height * width

    # 직사각형이 차지하는 넓이의 총합이 정수값이라면 정수로 변환
    if answer == int(answer):
        answer = int(answer)

    # 소수점 둘째자리까지 반올림하여 반환
    return round(answer, 2)
