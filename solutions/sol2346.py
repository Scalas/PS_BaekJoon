import sys
from collections import deque

input = sys.stdin.readline


# 2346 풍선 터뜨리기
# n 개의 풍선과 그 안에 들어있는 종이의 값(0이 아닌 정수)이 주어지고
# 1번 풍선을 터트리는 것으로 시작하여 풍선 안의 종이의 숫자만큼 인덱스를 이동하여
# 그자리의 풍선을 터트리길 반복할 때, 모든 풍선이 터지기까지 터지는 풍선의 순서를 구하는 문제
# 단, 풍선이 터진 자리는 이동시 세지 않는다.
def sol2346():
    n = int(input())
    nums = list(map(int, input().split()))
    q = deque()
    for i in range(n):
        q.append((i + 1, nums[i]))

    # 양방향 큐를 사용하여 해결 가능
    # 순환 큐도 사용 가능하지만 파이썬에서는 비효율적
    answer = []
    while q:
        target, move = q.popleft()
        answer.append(target)

        if not q:
            break

        if move > 0:
            for _ in range(move - 1):
                q.append(q.popleft())
        else:
            for _ in range(-move):
                q.appendleft(q.pop())

    return ' '.join(map(str, answer))
