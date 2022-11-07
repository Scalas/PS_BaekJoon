import sys
from collections import deque

input = sys.stdin.readline


# 15828 Router
# 버퍼크기가 n인 라우터에 패킷이 쌓이고 소모되기를 반복한 후
# 버퍼에 남아있는 패킷의 번호를 순서대로 출력하는 문제
def sol15828():
    q = deque()
    cap = int(input())
    while True:
        req = int(input())
        if req == 0:
            q.popleft()
        elif req > 0:
            if len(q) < cap:
                q.append(req)
        else:
            break
    return ' '.join(map(str, q))
