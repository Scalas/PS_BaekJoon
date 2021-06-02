import sys
import heapq

input = sys.stdin.readline


# 11279 최대힙
# 최대힙 구현문제
# heapq 모듈을 사용하여 간단하게 구현 가능
def sol11279():
    n = int(input())
    cmds = [int(input()) for _ in range(n)]
    q = []
    answer = []
    for cmd in cmds:
        if (cmd == 0):
            answer.append('0' if not q else str(-heapq.heappop(q)))
        else:
            heapq.heappush(q, -cmd)
    print('\n'.join(answer))
