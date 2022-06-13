import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 15459 Haybale Feast
# n개의 건초의 맛과 매운정도가 순서대로 주어지고
# 이중 연속된 건초들의 맛의 합이 m이상이 되도록 하면서 매운 정도중 최댓값이 최소가 되게 하려 할 때
# 매운 정도의 최댓값의 최솟값을 구하는 문제
def sol15459():
    n, m = map(int, input().split())
    hay = [list(map(int, input().split())) for _ in range(n)]

    # 연속된 건초의 시작 위치, 끝위치 + 1
    s, e = 0, 1

    # 맛의 합
    flavor = hay[0][0]

    # 매운 정도의 최댓값을 구하기 위한 힙
    spicy = [(-hay[0][1], 0)]

    # i번째 건초가 spicy 힙에서 제거됨을 표시
    removed = [False] * n

    # spicy의 최솟값
    answer = 10 ** 9

    while e <= n:
        # flavor가 아직 m 이상이 아닐경우
        if flavor < m:
            # 더이상 flavor를 늘릴 수 없다면 탐색 종료
            if e == n:
                break

            # 건초를 하나 더 포함시킴
            flavor += hay[e][0]
            heappush(spicy, (-hay[e][1], e))
            e += 1

        # flavor가 m 이상일 경우
        else:
            # 제거된 건초를 실제로 heap에서 제거(lazy deletion)
            while spicy and removed[spicy[0][1]]:
                heappop(spicy)

            # spicy의 최솟값 갱신
            answer = min(answer, -spicy[0][0])

            # 왼쪽 끝의 건초를 제거
            removed[s] = True
            flavor -= hay[s][0]
            s += 1
    return answer
