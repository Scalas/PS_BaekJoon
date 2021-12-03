import sys

input = sys.stdin.read


# 10768 특별한 날
# 월과 일이 주어졌을 때 특정 일자(2월 18일)보다 전인지 후인지 또는 당일인지 구하는 문제
def sol10768():
    m, d = map(int, input().split())
    if m < 2:
        return 'Before'
    if m > 2:
        return 'After'
    if d < 18:
        return 'Before'
    if d > 18:
        return 'After'
    return 'Special'
