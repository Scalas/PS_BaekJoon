import sys
from heapq import heappush, heappop


# 1655 가운데를 말해요
# 힙을 활용한 중간값 찾기 문제
def sol1655():
    maxq, minq = [], []
    n, *nums = map(int, sys.stdin.read().split())
    answer = []
    for num in nums:
        # 최대 힙이 비어있거나 수가 최대 힙의 최댓값 이상이라면 최대힙에 heappush
        if not maxq or num <= -maxq[0]:
            heappush(maxq, -num)
        # 그렇지 않다면 최소 힙에 heappush
        else:
            heappush(minq, num)

        diff = len(maxq) - len(minq)
        # 두 힙의 크기차이가 1보다 커지면 균형을 맞추고 크기차이를 0으로 세팅
        # maxq가 minq보다 2 크다면 maxq에서 원소 하나를 제거하여 minq에 넣어준다
        if diff == 2:
            heappush(minq, -heappop(maxq))
            diff = 0
        # minq가 maxq보다 2 크다면 minq에서 원소 하나를 제거하여 maxq에 넣어준다
        elif diff == -2:
            heappush(maxq, -heappop(minq))
            diff = 0

        # 두 힙의 크기차이가 없거나 maxq쪽이 크면 maxq의 최댓값이 중간값
        # 그렇지 않다면 minq의 최솟값이 중간값
        answer.append(-maxq[0] if diff >= 0 else minq[0])

    return '\n'.join(map(str, answer))
