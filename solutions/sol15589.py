import sys
from collections import defaultdict

input = sys.stdin.readline


# 15589 Lifeguards (Silver)
# n명의 라이프가드의 시프트시간 u, v가 주어지고(총 v - u시간의 시프트를 커버)
# 라이프가드중 한 명을 해고해야할 때
# 남은 라이프가드들이 커버 가능한 최대 시프트시간을 구하는 문제
def sol15589():
    n = int(input())

    # 모든 라이프가드의 시프트시간을 표시
    acc = defaultdict(int)
    lifeguards = []
    for _ in range(n):
        u, v = map(int, input().split())
        acc[u] += 1
        acc[v] -= 1
        lifeguards.append((u, v))

    # 누적합으로 각 시간대를 커버 가능한 인원의 수를 구함
    keys = sorted(acc.keys())
    for i in range(len(keys) - 1):
        cur = keys[i]
        nxt = keys[i + 1]
        acc[nxt] = acc[nxt] + acc[cur]

    # 모든 시간대의 인원수를 최대 2로 고정
    for i in range(len(keys)):
        cur = keys[i]
        acc[cur] = min(acc[cur], 2)

    # 전체 커버시간
    total = 0

    # 다시한번 누적합으로 구간별 커버되는 인원의 합을 구함
    # 단, 3 명 이상의 인원이 그 시간대를 커버 가능하다면 2명인 것으로 계산
    cover_time = defaultdict(int)
    cover_time[keys[0]] = 0
    for i in range(1, len(keys)):
        pre = keys[i - 1]
        cur = keys[i]
        cover_time[cur] = cover_time[pre] + (cur - pre) * acc[pre]
        if acc[pre]:
            total += (cur - pre)

    # 모든 라이프가드중 손실시간이 가장 작은 라이프가드를 해고
    # 그 라이프가드의 손실시간만큼 total에서 제외
    min_loss = total
    for u, v in lifeguards:
        loss = (v - u) * 2 - (cover_time[v] - cover_time[u])
        min_loss = min(min_loss, loss)

    # 전체 커버시간에서 라이프가드를 한 명 해고할 때 최소 손실시간을 빼줌
    return total - min_loss
