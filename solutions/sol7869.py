import sys
import math

input = sys.stdin.read


# 7869 두 원
# 두 원의 교차범위의 면적을 구하는 문제
# 제 2 코사인 법칙과 역삼각함수를 활용하는 문제이다.
def sol7869():
    # 두 원의 중점의 좌표와 반지름 길이
    x1, y1, r1, x2, y2, r2 = map(float, input().split())

    # 두 원의 중점 사이의 거리
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

    # 두 원이 외접하거나 떨어져있는 경우
    if d >= r1 + r2:
        return 0

    # 두 원이 내접하거나 포함관계인 경우
    if d <= abs(r1 - r2):
        return round(math.pi * min(r1, r2) ** 2, 3)

    # 두 원이 두 개의 교점을 가지는 경우
    # 공식에 따라 두 내각을 구한 뒤 교차면적을 소수점 넷째자리에서 반올림하여 반환
    a1, a2 = 2 * math.acos((d ** 2 + (r1 ** 2 - r2 ** 2)) / (2 * r1 * d)), 2 * math.acos(
        (d ** 2 - (r1 ** 2 - r2 ** 2)) / (2 * r2 * d))
    return round(1 / 2 * (r1 ** 2 * (a1 - math.sin(a1)) + r2 ** 2 * (a2 - math.sin(a2))), 3)


# 반올림 함수
def round(num, digit):
    # 자릿수만큼 10을 곱한 뒤 소수점자리가 5 이상이라면 1을 더해준다
    k = 10 ** digit
    res = num * k
    if res - int(res) >= 0.5:
        res += 1

    # 정수변환 후 자릿수만큼 10을 나누어 반환
    return int(res) / k
