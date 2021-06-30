import sys
from collections import deque

input = sys.stdin.readline


# 1021 회전하는 큐
# 순환하는 큐에서 숫자를 원하는 순서대로 뽑아내기 위해
# 수행해야할 최소한의 좌, 우 이동연산 횟수를 구하는 문제

# deque 모듈을 사용하면 간단하게 풀 수 있다.
# 뽑으려는 숫자의 인덱스를 탐색한 뒤 좌우 이동중 어느쪽이 가까운지 계산하여 더한다
# deque 모듈을 사용하지않고 단순히 리스트에 슬라이싱과 + 연산을 사용하는 풀이도 가능하다
def sol1021():
    n, m = map(int, input().split())
    l = deque([i for i in range(1, n + 1)])
    answer = 0
    for num in map(int, input().split()):
        # 뽑으려는 수의 인덱스 탐색
        idx = l.index(num)

        # 이동이 필요없을 경우 pop
        if (idx == 0):
            l.popleft()
            continue

        # 이동이 필요한 경우 연산횟수가 더 적은 방향으로 회전
        left = idx
        right = len(l) - idx
        if left < right:
            answer += left
            for _ in range(left):
                l.append(l.popleft())
            l.popleft()
        else:
            answer += right
            for _ in range(right - 1):
                l.appendleft(l.pop())
            l.pop()
    print(answer)


# 리스트 슬라이싱만을 이용한 풀이
def sol1021_2():
    n, m, *select = map(int, sys.stdin.read().split())
    q = list(range(n, 0, -1))
    answer = 0
    for s in select:
        l = len(q) - q.index(s) -1
        if l == 0:
            q.pop()
            continue

        r = len(q) - l
        if l < r:
            answer += l
        else:
            answer += r
        q = q[r:] + q[:r - 1]
    print(answer)
