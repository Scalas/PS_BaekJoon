import sys
import heapq

input = sys.stdin.read


# 1927 최소 힙
# 최소힙 구현문제

# 직접 힙을 구현한 풀이
# 리스트에 push, pop 연산만을 구현하여 해결
class Heap:
    def __init__(self):
        self.q = []

    def push(self, e):
        self.q.append(e)
        idx = len(self.q) - 1
        while idx > 0:
            parent = (idx - 1) // 2 if idx % 2 != 0 else (idx - 2) // 2
            if (parent >= 0 and self.q[parent] > e):
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
            if (l < len(self.q) and self.q[l] < self.q[idx]):
                t = l
            if (r < len(self.q) and self.q[r] < self.q[idx]):
                if t == None or self.q[r] < self.q[t]:
                    t = r
            if not t:
                break
            self.q[idx], self.q[t] = self.q[t], self.q[idx]
            idx = t
        return ret


def sol1927():
    cmd = list(map(int, input().splitlines()))[1:]
    heap = Heap()
    answer = []
    for c in cmd:
        if (c == 0):
            answer.append(heap.pop())
        else:
            heap.push(c)
    print('\n'.join(answer))


# heapq 모듈을 사용한 풀이
# 직접 힙을 구현하는 것 보다 훨씬 빠른 속도를 보인다
def sol1927_2():
    cmd = list(map(int, input().splitlines()))[1:]
    heap = []
    answer = []
    for c in cmd:
        if (c == 0):
            answer.append('0' if not heap else str(heapq.heappop(heap)))
        else:
            heapq.heappush(heap, c)
    print('\n'.join(answer))
