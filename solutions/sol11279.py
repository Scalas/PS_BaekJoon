import sys
import heapq

input = sys.stdin.readline


# 11279 최대힙
# 최대힙 구현문제

# 직접 최대 힙을 구현한 풀이
# 리스트에 push, pop 연산만을 구현하여 해결
class Heap:
    def __init__(self):
        self.q = []

    def push(self, e):
        self.q.append(e)
        idx = len(self.q) - 1
        while idx > 0:
            parent = (idx - 1) // 2 if idx % 2 != 0 else (idx - 2) // 2
            if (parent >= 0 and self.q[parent] < e):
                self.q[parent], self.q[idx] = e, self.q[parent]
                idx = parent
            else:
                break

    def pop(self):
        if not self.q:
            return '0'
        if len(self.q) == 1:
            return str(self.q.pop())

        ret = str(self.q[0])
        self.q[0] = self.q.pop()
        idx = 0
        while True:
            l, r = idx * 2 + 1, idx * 2 + 2
            t = None
            if (l < len(self.q) and self.q[l] > self.q[idx]):
                t = l
            if (r < len(self.q) and self.q[r] > self.q[idx]):
                if t == None or self.q[r] > self.q[t]:
                    t = r
            if not t:
                break
            self.q[idx], self.q[t] = self.q[t], self.q[idx]
            idx = t
        return ret


def sol11279():
    n = int(input())
    cmds = [int(input()) for _ in range(n)]
    heap = Heap()
    size = 0
    answer = []
    for cmd in cmds:
        if cmd == 0:
            answer.append(heap.pop())
        else:
            heap.push(cmd)

    print('\n'.join(answer))


# heapq 모듈을 사용하여 간단하게 구현 가능
# 직접 힙을 구현한 것 보다 훨씬 빠른 속도를 보임
def sol11279_2():
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
