import sys
import heapq


def sol11286():
    n, *cmd = map(int, sys.stdin.read().split())
    pheap, mheap = [], []
    answer = []
    for c in cmd:
        if c > 0:
            heapq.heappush(pheap, c)
        elif c < 0:
            heapq.heappush(mheap, -c)
        else:
            if not pheap and not mheap:
                answer.append('0')
            elif not pheap:
                answer.append(str(-heapq.heappop(mheap)))
            elif not mheap:
                answer.append(str(heapq.heappop(pheap)))
            elif pheap[0] < mheap[0]:
                answer.append(str(heapq.heappop(pheap)))
            else:
                answer.append(str(-heapq.heappop(mheap)))
    print('\n'.join(answer))
