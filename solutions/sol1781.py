import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 1781 컵라면
# n개의 숙제의 데드라인(시간)과 숙제를 했을 때 받을 수 있는 컵라면의 수가 주어지고
# 1시간당 하나의 문제만 풀 수 있다고 할 때
# 얻을 수 있는 컵라면의 최대갯수를 구하는 문제
def sol1781():
    n = int(input())
    work = [list(map(int, input().split())) for _ in range(n)]
    work.sort()

    # 숙제를 데드라인이 짧은 것을 우선하여 힙에 삽입
    # 만약 삽입한 후의 힙의 길이가 데드라인보다 크다면
    # 가장 컵라면을 적개 받는 숙제 하나를 힙에서 제거
    proc = []
    for d, c in work:
        heappush(proc, c)
        if len(proc) > d:
            heappop(proc)

    # 힙에 남아있는 숙제의 컵라면 갯수의 합을 반환
    return sum(proc)
