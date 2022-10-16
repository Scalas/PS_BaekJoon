import sys
from heapq import heappush, heappop
from collections import deque

input = sys.stdin.readline


# 11003 최솟값 찾기
# 수열 s 의 s[i - l + 1] ~ s[i] 까지의 수 중 최솟값을 0 <= i < n 인 모든 i 에 대해 구하는 문제

# 풀이 1: heap의 lazy deletion 을 사용한 풀이
def sol11003():
    n, l = map(int, input().split())
    seq = list(map(int, input().split()))
    removed = [False] * n
    h = []
    answer = []

    for i in range(n):
        heappush(h, (seq[i], i))
        if i >= l:
            removed[i - l] = True
        while removed[h[0][1]]:
            heappop(h)
        answer.append(h[0][0])

    return ' '.join(map(str, answer))


# 풀이 2: deque를 사용한 풀이
# 나중에 들어온 수 보다 큰 수는 어차피 최솟값 후보가 될 수 없기 때문에 큐에서 제거
# 제거되어야할 i - l 번째 수가 만약 현재 후보중 최솟값이라면 후보에서 그 수를 제거
# 최솟값 후보는 항상 들어온 순서를 유지하기 때문에 제거할 수가 후보중 최솟값이 아니라면 이미 제거된 것으로 볼 수 있음
def sol11003_2():
    n, l = map(int, input().split())
    seq = list(map(int, input().split()))
    q = deque()
    answer = []

    for i in range(n):
        num = seq[i]
        while q and q[-1] > num:
            q.pop()
        q.append(num)
        if i >= l and q[0] == seq[i - l]:
            q.popleft()
        answer.append(q[0])

    return ' '.join(map(str, answer))
