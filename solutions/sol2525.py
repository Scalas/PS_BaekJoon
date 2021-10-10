import sys

input = sys.stdin.read


# 2525 오븐 시계
# 현재시간과 조리에 걸리는 시간이 주어졌을때 완료시간을 구하는 문제
# 시간을 분단위로 변환하여 계산한 뒤 다시 시간단위와 분단위로 구분해주면 된다
# 24시를 넘어가면 0시부터 다시시작하는것에 주의
def sol2525():
    h, m, c = map(int, input().split())
    t = h * 60 + m + c
    return '%d %d' % (t//60 % 24, t % 60)
