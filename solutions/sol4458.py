import sys

input = sys.stdin.read


# 4458 첫 글자를 대문자로
# 주어진 문자열의 첫 글자를 대문자로 변환하여 출력하는 문제
def sol4458():
    n, *strings = input().splitlines()
    return '\n'.join(map(conv, strings))


def conv(string):
    sl = list(string)
    sl[0] = sl[0].upper()
    return ''.join(sl)
