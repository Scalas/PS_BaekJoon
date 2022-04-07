import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 13904 과제
# 과제의 d-day와 점수가 주어지고 d-day 이전에 과제를 끝내야 점수를 받을 수 있으며
# 하루에 하나의 과제를 완료할 수 있을 때, 얻을 수 있는 최대 점수를 구하는 문제
def sol13904():
    q = []
    works = [list(map(int, input().split())) for _ in range(int(input()))]
    
    # 과제를 d-day 순으로 오름차순 정렬
    works.sort()
    
    for u, v in works:
        # 정렬된 과제를 순차적으로 수행(힙큐에 삽입)
        heappush(q, v)
        
        # 수행한 과제의 d-day가 과제들을 수행하는데 걸린 날짜보다 작다면
        # 수행한 과제중 가장 점수가 적은 과제를 수행하지 않는 것으로 하여 모순을 해결
        if u < len(q):
            heappop(q)
    
    # 수행한 과제의 점수의 합산을 반환
    return sum(q)
