import sys

input = sys.stdin.readline


# 10845 큐
# 간단한 기능을 가진 큐를 구현하는 문제
# deque 모듈을 사용할 수도 있지만 연산의 수가 매우 적기 때문에
# 단순히 리스트를 사용하여 구현하였다.
def sol10845():
    q = []
    head = 0
    cnt = 0
    answer = []
    for _ in range(int(input())):
        cmd = input().split()
        if len(cmd) == 2:
            q.append(cmd[1])
            cnt += 1
        else:
            t = cmd[0][0]
            if t == 'p':
                if cnt:
                    answer.append(q[head])
                    head += 1
                    cnt -= 1
                else:
                    answer.append('-1')
            elif t == 'f':
                answer.append(q[head] if cnt else '-1')
            elif t == 'b':
                answer.append(q[-1] if cnt else '-1')
            elif t == 's':
                answer.append(str(cnt))
            else:
                answer.append('0' if cnt else '1')
    return '\n'.join(answer)
