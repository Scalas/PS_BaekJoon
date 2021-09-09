import sys
import heapq


# 11286 절댓값 힙
def sol11286():
    # 연산의 갯수 n, 연산리스트
    n, *cmd = map(int, sys.stdin.read().split())

    # 양수 힙과 음수 힙을 생성
    pheap, mheap = [], []

    # 연산의 결과 출력되는 값을 저장할 리스트
    answer = []

    for c in cmd:
        # 양수가 주어졌을 경우 양수 힙에 그대로 삽입
        if c > 0:
            heapq.heappush(pheap, c)

        # 음수가 주어졌을 경우 음수 힙에 - 를 취하여 삽입
        elif c < 0:
            heapq.heappush(mheap, -c)

        # 0이 주어졌을 경우 절댓값이 가장 작은 값을 출력
        else:
            # 두 힙이 모두 비어있다면 0
            if not pheap and not mheap:
                answer.append('0')

            # 어느 한쪽이 비어있다면 한쪽에서 pop 한 값을 출력
            elif not pheap:
                answer.append(str(-heapq.heappop(mheap)))
            elif not mheap:
                answer.append(str(heapq.heappop(pheap)))

            # 둘다 비어있지 않다면 두 힙의 절댓값이 가장 작은 수 중 보다 절댓값이 작은 쪽을 출력
            elif pheap[0] < mheap[0]:
                answer.append(str(heapq.heappop(pheap)))
            else:
                answer.append(str(-heapq.heappop(mheap)))

    # 출력형식에 맞춰 정답리스트 반환
    print('\n'.join(answer))
