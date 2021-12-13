import sys

input = sys.stdin.readline


# 11816 8진수, 10진수, 16진수
# 0으로 시작하는 수는 8진수, 0x로 시작하는 수는 16진수, 그 외는 10진수로 간주하여
# 주어진 수를 10진수로 변환한 값을 구하는 문제
def sol11816():
    n = input()
    base = 10
    if len(n) > 1 and n[0] == '0':
        if n[1] == 'x':
            base = 16
        else:
            base = 8
    return int(n, base)
