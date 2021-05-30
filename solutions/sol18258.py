import sys
from collections import deque

input = sys.stdin.read


# 18258 큐 2
# 정수를 저장하는 간단한 큐의 구현
# 파이썬의 deque 모듈을 사용하면 간단하게 풀 수 있다
def sol18258():
    q = deque()
    answer = []
    for i in input().splitlines()[1:]:
        spl = i.split()
        cmd = spl[0]
        if (cmd == 'push'):
            q.append(spl[1])
        elif (cmd == 'pop'):
            answer.append('-1' if not q else q.popleft())
        elif (cmd == 'size'):
            answer.append(str(len(q)))
        elif (cmd == 'empty'):
            answer.append('0' if q else '1')
        elif (cmd == 'front'):
            answer.append('-1' if not q else q[0])
        elif (cmd == 'back'):
            answer.append('-1' if not q else q[-1])
    print('\n'.join(answer))


# 모듈을 사용하지 않고 직접 링크드리스트로 구현한 풀이지만 Python 3으로는 속도가 느려 시간초과(PyPy3으론 통과)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.siz = 0

    def push(self, e):
        node = Node(e)
        if(self.siz==0):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.siz += 1

    def pop(self):
        if(self.siz==0):
            return '-1'
        res = self.head.data
        self.head = self.head.next
        self.siz -= 1
        if(self.siz==0):
            self.tail = None
        return res

    def size(self):
        return str(self.siz)

    def empty(self):
        return '0' if self.siz>0 else '1'

    def front(self):
        return '-1' if self.siz == 0 else self.head.data

    def back(self):
        return '-1' if self.siz == 0 else self.tail.data


def sol18258_2():
    q = Queue()
    answer = []
    for i in input().splitlines()[1:]:
        spl = i.split()
        cmd = spl[0]
        if (cmd == 'push'):
            q.push(spl[1])
        elif (cmd == 'pop'):
            answer.append(q.pop())
        elif (cmd == 'size'):
            answer.append(q.size())
        elif (cmd == 'empty'):
            answer.append(q.empty())
        elif (cmd == 'front'):
            answer.append(q.front())
        elif (cmd == 'back'):
            answer.append(q.back())
    print('\n'.join(answer))


# 단순히 리스트에 append 해나가면서 pop 할때마다 front 를 나타내는 인덱스를 증가시키는 방식
# 링크드리스트를 이용한 구현보다 속도가 빠르지만 pop 한 데이터가 실제로 사라지는 것이 아니기 때문에
# 공간낭비가 심하다
def sol18258_3():
    q = []
    fidx = 0
    bidx = -1
    answer = []
    for i in input().splitlines()[1:]:
        spl = i.split()
        cmd = spl[0]
        if (cmd == 'push'):
            q.append(spl[1])
            bidx += 1
        elif (cmd == 'pop'):
            if(fidx > bidx):
                answer.append('-1')
            else:
                answer.append(q[fidx])
                fidx += 1
        elif (cmd == 'size'):
            answer.append(str(bidx-fidx+1))
        elif (cmd == 'empty'):
            answer.append('1' if fidx > bidx else '0')
        elif (cmd == 'front'):
            answer.append('-1' if fidx > bidx else q[fidx])
        elif (cmd == 'back'):
            answer.append('-1' if fidx > bidx else q[bidx])
    print('\n'.join(answer))