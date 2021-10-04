import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 1516 게임 개발
# 건물들을 짓기 위해 필요한 시간과 먼저 지어야할 건물의 리스트가 주어졌을 때
# 각 건물이 완성되기까지 걸리는 시간을 구하는 문제
# 여러 건물의 건설을 동시에 진행하는 것도 가능

# 위상정렬을 활용하여 해결 가능한 문제
def sol1516():
    # 건물의 갯수
    n = int(input())

    # 각 건물의 건설에 들어가는 시간
    cost = [0] * (n + 1)

    # g[a] 리스트에 b 가 있다면 b를 짓기 위해서는 a가 먼저 지어져야 한다
    g = [[] for _ in range(n + 1)]

    # 각 노드(건물)의 진입 차수
    degree = [0] * (n + 1)

    # 건물들의 관계를 그래프로 나타내고 비용과 진입차수를 구한다
    for i in range(1, n + 1):
        c, *pre = map(int, input().split())
        cost[i] = c
        for p in pre[:-1]:
            g[p].append(i)
            degree[i] += 1

    # 최초에 진입 차수가 0인 건물들을 큐에 삽입
    q = []
    for i in range(1, n + 1):
        if not degree[i]:
            heappush(q, (cost[i], i))

    # 각 건물이 완성될 때 까지 걸리는 시간
    answer = [0] * n

    # heapq 를 사용하여 진입 차수가 0인 건물 중 건설에 드는 시간이 적은 순으로 탐색
    while q:
        # 걸리는 시간, 건물 번호
        time, cur = heappop(q)

        # 건축에 걸리는 시간을 저장
        answer[cur - 1] = time

        # 다른 건물들의 진입차수의 변경을 반영
        for nxt in g[cur]:
            degree[nxt] -= 1

            # 진입 차수가 0이된 건물이 있다면 큐에 삽입
            # 추가되는 건물의 건축완료시간은 현재 건물의 건축완료시간 + 해당 건물의 건축시간이 된다.
            if not degree[nxt]:
                heappush(q, (time + cost[nxt], nxt))

    # 출력 형식에 맞춰 정답 리스트 반환
    return '\n'.join(map(str, answer))
