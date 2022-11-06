import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline


# 13975 파일 합치기 3
# n개의 파일의 크기가 주어지고 두 파일씩 합쳐 하나의 파일로 만들려 할 때
# 모든 파일을 합치는데 드는 최소비용을 구하는 문제
# 단, 파일을 합치는 비용은 합칠 두 파일의 크기의 합이다
def sol13975():
    answer = []
    # 매번 가장 작은 두 페이지를 합치도록 하면 최소 비용으로 합칠 수 있음
    for _ in range(int(input())):
        cost = 0
        input()
        pages = list(map(int, input().split()))
        heapify(pages)
        while len(pages) > 1:
            merged_page = heappop(pages) + heappop(pages)
            cost += merged_page
            heappush(pages, merged_page)
        answer.append(cost)
    return '\n'.join(map(str, answer))
