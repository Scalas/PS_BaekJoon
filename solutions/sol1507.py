import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10 ** 9


# 1507 궁금한 민호
# n개의 도시간의 최단거리가 인접행렬 형태로 주어졌을 때
# 최소 갯수의 간선으로 해당 최단거리 행렬을 만족시킬 경우
# 간선의 가중치의 합을 구하는 문제
def sol1507():
    n = int(input())
    g = [[] for _ in range(n)]
    sp = [list(map(int, input().split())) for _ in range(n)]

    # 노드 i, j 사이의 최단거리를 간선 후보로 저장
    cand = []
    for i in range(n-1):
        for j in range(i+1, n):
            cand.append([sp[i][j], i, j])

    # 거리기준 오름차순 정렬
    cand.sort()

    # i j간 직접 간선 추가 여부를 검토
    answer = 0
    for d, i, j in cand:
        # 지금까지 추가된 간선만으로 i, j간의 최단 거리를 계산
        dp = [INF] * n
        dp[i] = 0
        q = [(0, i)]
        while q:
            dst, cur = heappop(q)
            if dst > dp[cur]:
                continue

            for nxt, dist in g[cur]:
                if dst + dist < dp[nxt]:
                    dp[nxt] = dst + dist
                    heappush(q, (dp[nxt], nxt))

        # 만약 i j간의 최단거리가 이미 d를 만족한다면 추가하지 않음
        if dp[j] == d:
            continue

        # i, j간의 최단거리가 d보다 작을 경우 불가능한 케이스
        if dp[j] < d:
            return -1

        # 간선 추가
        # 간선의 가중치 합에 추가
        g[i].append((j, d))
        g[j].append((i, d))
        answer += d

    return answer
