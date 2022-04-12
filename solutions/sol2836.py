import sys
from collections import deque

input = sys.stdin.readline


# 2836 수상 택시
# 0에서 m 사이의 좌표상에서 n명의 승객들의 탑승위치와 하차위치가 주어졌을 때
# 0에서 출발한 택시가 모든 손님들을 목적지에 데려다준 뒤 m에서 운행을 마치기 위해
# 필요한 최소 이동거리를 구하는 문제
def sol2836():
    n, m = map(int, input().split())
    # 탑승위치보다 하차위치가 나중이라면 어차피 자연스럽게 내리게 되기 때문에 스킵
    q = []
    for _ in range(n):
        u, v = map(int, input().split())
        if u > v:
            q.append([u, v])

    # 하차 위치를 기준으로 정렬
    q.sort(key=lambda x: x[1])

    answer = 0
    cur = 0
    taxi = deque()
    for u, v in q:
        # 이미 탑승한 승객인 경우 하차위치를 taxi에 삽입
        if u <= cur:
            taxi.append(v)
        else:
            # 다음 승객의 하차위치가 현재위치 이후일 경우
            # 현재 위치 이전에 하차할 승객들을 처리
            if cur < v and taxi:
                rewind = taxi.popleft()
                answer += (cur - rewind) * 2
                while taxi and taxi[0] <= cur:
                    taxi.popleft()

            # 다음 승객의 하차위치를 taxi에 삽입
            taxi.append(v)
            answer += (u - cur)
            cur = u

    # 아직 탑승중인 승객을 모두 하차시킨 뒤 m으로 이동
    if taxi:
        answer += ((m - taxi.popleft()) * 2 - (m - cur))

    return answer
