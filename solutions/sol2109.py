import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 2109 순회 강연
# n개의 강연의 강연료와 d-day가 주어지고 하루에 하나의 강연만 가능할 때
# 얻을 수 있는 강연료의 최댓값을 구하는 문제
def sol2109():
    n = int(input())

    # d-day 순으로 정렬
    q = [list(map(int, input().split())) for _ in range(n)]
    q.sort(key=lambda x: x[1])

    # 참여할 강연의 강연료 목록(힙)
    work = []
    for pay, day in q:
        # work의 길이 = 이전까지 참여한 강연의 갯수 = 지난 일수
        # work의 길이보다 d-day가 크다면 그냥 참여할 수 있음(힙에 삽입)
        if len(work) < day:
            heappush(work, pay)

        # work의 길이보다 d-day가 작다면
        # 강연료 목록에 이번 강연의 강연료를 삽입한 후
        # 가장 적은 강연료를 추출(이번 강연의 강연료가 빠질 수도 있음)
        else:
            heappush(work, pay)
            heappop(work)

    # 강연료의 합 반환
    return sum(work)
