import sys
from math import ceil

input = sys.stdin.readline


# 13458 시험 감독
# 각 시험장마다 최대 1명의 총감독과 여럿의 부감독을 둘 수 있고
# 총감독의 감시가능 인원수가 b, 부감독은 c 일 때
# 모든 시험장을 감시하기위해 필요한 감독의 수를 구하는 문제
def sol13458():
    n = int(input())
    a_list = list(map(int, input().split()))
    b, c = map(int, input().split())

    # 감독관 한명의 감독가능 인원수가 응시자의 수보다 많은 경우에 주의
    return sum([1 if a <= b else ceil((a-b)/c) + 1 for a in a_list])
