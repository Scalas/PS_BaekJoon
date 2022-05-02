import sys
from collections import defaultdict

input = sys.stdin.readline
# days[i] 는 i월까지의 모든 일수를 더한 값(평년기준)
days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]


# 9203 호텔 예약
# 2013년 1월 1일 00:00 부터 2017년 1월 1일 00:00 이전까지의 시간대에서
# 호텔 객실의 입실시간과 퇴실시간의 리스트가 주어졌을 때
# 모든 예약에 대해 방을 배정하기 위해 필요한 방의 갯수를 구하는 문제
# 단, 방을 사용하기 전에는 반드시 청소를 해야한다(청소에는 반드시 주어진 c 만큼의 시간이 걸린다)
def sol9203():
    answers = []
    for _ in range(int(input())):
        b, c = map(int, input().split())

        # reserv[i] 는 시간이 i일 때 필요한 방의 갯수의 증감치
        reserv = defaultdict(int)

        # 모든 예약에 대해 입실시간, 퇴실시간을 파싱하여 reserv를 작성
        for _ in range(b):
            _, sdate, stime, edate, etime = input().split()
            start, end = stot(sdate, stime)-c, stot(edate, etime)
            reserv[start] += 1
            reserv[end] -= 1

        # 누적합을 사용하여 동시에 사용해야할 방의 최대 갯수를 구함
        answer = 0
        acc = 0
        for t, v in sorted(reserv.items()):
            acc += v
            answer = max(answer, acc)

        answers.append(answer)

    return '\n'.join(map(str, answers))


# datetime 문자열 파싱
def stot(date, time):
    y, m, d = map(int, date.split('-'))
    hh, mm = map(int, time.split(":"))

    # 2013년 1월 1일부터의 일수
    day = 0
    day += (y - 2013) * 365     # 2013년으로부터 지난 년수 * 365
    day += days[m - 1]          # days[1월로부터 지난 달수]
    if y == 2016 and m >= 3:    # 윤년(2016)이며 2월이 지났을 경우 1일 추가
        day += 1
    day += (d - 1)              # 오늘을 제외한 일수

    # 분단위까지 계산하여 반환
    return (day * 24 + hh) * 60 + mm
