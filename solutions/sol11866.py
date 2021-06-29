import sys
from collections import deque

input = sys.stdin.readline


# 11866 요세푸스 문제 0
# 1부터 n 까지의 숫자가 원형을 이루고있을때 k 칸만큼 이동하며 숫자를 하나씩 지워
# 모든 숫자를 지운 뒤 지워진 순서대로 숫자를 출력하는 문제

# 1부터 n 까지의 숫자가 담긴 리스트에서 대상 인덱스를 갱신해가며 지우는 방식
# k번 이동하고 지워야하기 때문에 idx + k,  기존 idx 위치의 숫자는 삭제되었기 때문에 -1
# idx 의 범위가 리스트를 벗어나면 안되기 때문에 % len(l)
# 숫자를 하나씩 삭제하는 작업이 n 번 발생하며 pop(idx)의 복잡도는 O(N)이기 때문에
# 복잡도는 O(N^2)
def sol11866():
    n, k = map(int, input().split())
    l = [i for i in range(1, n+1)]
    idx = 0
    answer = []
    while l:
        idx = (idx+k-1)%len(l)
        answer.append(l.pop(idx))
    print(answer)


# 환형 링크드리스트를 활용한 풀이
# 삭제연산은 O(1)로 이루어지지만 삭제할 위치를 탐색하는 시간이 O(NK) 이기 때문에
# k의 크기가 충분히 작지 않으면 1번 풀이보다 떨어지는 성능을 보인다
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Circular_Queue:
    def __init__(self):
        self.cur = None
        self.size = 0

    def push(self, e):
        node = Node(e)
        if self.cur == None:
            node.next = node
            node.prev = node
            self.cur = node
        else:
            node.next = self.cur.next
            node.prev = self.cur
            self.cur.next.prev = node
            self.cur.next = node
            self.cur = node
        self.size += 1

    def pop(self):
        res = self.cur.data
        self.cur.prev.next = self.cur.next
        self.cur.next.prev = self.cur.prev
        self.cur = self.cur.prev
        self.size -= 1
        return res

    def move(self, cnt):
        for _ in range(cnt):
            self.cur = self.cur.next

    def empty(self):
        return self.size == 0


def sol11866_2():
    n, k = map(int, input().split())
    q = Circular_Queue()
    for i in range(1, n + 1):
        q.push(str(i))

    answer = []
    while (not q.empty()):
        q.move(k)
        answer.append(q.pop())

    print('<' + ', '.join(answer) + '>')


# 큐를 사용한 풀이
# 2번 풀이와 같은 복잡도를 가진다
def sol11866_3():
    n, k = map(int, input().split())
    q = deque([str(i) for i in range(1, n+1)])
    answer = []
    while q:
        for _ in range(k-1):
            q.append(q.popleft())
        answer.append(q.popleft())
    print('<'+', '.join(answer)+'>')


# 큐를 이용한 풀이를 리스트 연산으로 대체한 풀이
def sol11866_4():
    n, k = map(int, sys.stdin.readline().split())
    seq = [*range(1, n+1)]
    answer = []
    while seq:
        i = (k-1) % len(seq)
        answer.append(str(seq[i]))
        seq = seq[i+1:] + seq[:i]
    print('<' + ', '.join(answer) + '>')
