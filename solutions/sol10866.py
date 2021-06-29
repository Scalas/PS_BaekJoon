import sys
from collections import deque

input = sys.stdin.read


# 앞 뒤로 삽입/삭제가 가능한 양방향 큐, 데크를 구현하는 문제
# 연결리스트로 구현할 수 있지만 여기서는 deque 모듈을 사용하여 구현
def sol10866():
    q = deque()
    answer = []
    for line in input().splitlines()[1:]:
        cmd = line.split()
        if cmd[0] == 'push_front':
            q.appendleft(cmd[1])

        elif cmd[0] == 'push_back':
            q.append(cmd[1])

        elif cmd[0] == 'pop_front':
            answer.append('-1' if not q else q.popleft())

        elif cmd[0] == 'pop_back':
            answer.append('-1' if not q else q.pop())

        elif cmd[0] == 'size':
            answer.append(str(len(q)))

        elif cmd[0] == 'empty':
            answer.append('0' if q else '1')

        elif cmd[0] == 'front':
            answer.append('-1' if not q else q[0])

        elif cmd[0] == 'back':
            answer.append('-1' if not q else q[-1])

    print('\n'.join(answer))
