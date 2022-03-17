import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 13334 철로
# (시작점, 끝점)으로 이루어진 좌표 n개와 철로의 길이 d가 주어졌을 때
# 길이 d의 철로 안에 시작점과 끝점이 모두 들어가는 좌표 수의 최댓값을 구하는 문제
def sol13334():
    # 좌표의 수
    n = int(input())

    # 좌표를 시작점 < 끝점이 되도록 변환하여 삽입
    pos = []
    for _ in range(n):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        pos.append((u, v))

    # 철로의 길이
    d = int(input())

    # 시작점과 끝점의 길이가 d를 넘는 좌표를 제거
    pos = [p for p in pos if p[1]-p[0] <= d]
    n = len(pos)

    # 좌표를 끝점을 기준으로 오름차순 정렬
    pos.sort(key=lambda x:x[1])

    answer = 0
    q = []
    for p in pos:
        # p는 끝값이 가장 우측에 있는 좌표이며
        # q[0]은 큐에 들어있는 좌표중 시작점이 가장 좌측에 있는 좌표

        # 먼저 p를 큐에 삽입
        heappush(q, p)

        # 구간의 길이(p[1] - q[0][0])가 d보다 클 경우
        # 이전까지의 큐의 길이로 answer를 갱신하고
        # 구간의 길이가 d이하가 될 때 까지 시작점이 가장 작은 좌표를 pop
        if p[1] - q[0][0] > d:
            answer = max(answer, len(q)-1)
            while p[1] - q[0][0] > d:
                heappop(q)

    # 마지막 큐의 길이로 answer를 최종적으로 갱신
    answer = max(answer, len(q))

    return answer
