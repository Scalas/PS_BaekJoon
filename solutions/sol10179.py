import sys

input = sys.stdin.read


# 10179 쿠폰
# 주어진 액수들의 20퍼센트 할인가를 구하는 문제
def sol10179():
    return '\n'.join(map(lambda x: '$%.2f' % (float(x) * 0.8), input().split()[1:]))
