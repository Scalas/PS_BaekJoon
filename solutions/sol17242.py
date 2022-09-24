import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10 ** 9


# 17242 Kaka & Bebe
# n 개의 노드와 m 개의 간선으로 이루어진 그래프가 있고
# 각 간선에는 c 마리의 kaka와 d 마리의 bebe가 있다.
# 0번 노드에서 n-1번 노드까지 kaka 나 bebe 의 총합이 각각 1000을 넘지 않으며 이동할 때
# 경로상의 kaka의 총합과 bebe의 총합을 곱한 값(스트레스)의 최솟값을 구하는 문제
def sol17242():
    n, m = map(int, input().split())

    # 간선 정보
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c, d = map(int, input().split())
        g[a].append([b, c, d])
        g[b].append([a, c, d])

    # dp[i][j] 는 노드 0부터 i 까지 카카의 수가 j 일 때 베베의 수의 최솟값
    dp = [[INF] * 1001 for _ in range(n)]
    shortest = [(INF, INF)] * n
    dp[0][0] = 0
    shortest[0] = (0, 0)

    # (i, j, k) 는 카카의 수가 i, 베베의 수가 j 상태인 노드 k
    q = [(0, 0, 0)]
    while q:
        kaka, bebe, cur = heappop(q)
        sk, sb = shortest[cur]

        # 노드 cur 의 kaka 의 수에 대한 bebe 의 수가 최솟값이 아닌 경우 continue
        if dp[cur][kaka] < bebe:
            continue

        if kaka > sk and bebe > sb:
            continue

        for nxt, edge_kaka, edge_bebe in g[cur]:
            # 노드 nxt 로 갔을 때 kaka의 수와 bebe의 수
            next_kaka, next_bebe = kaka + edge_kaka, bebe + edge_bebe
            nsk, nsb = shortest[nxt]

            # 둘 중 하나라도 1000을 넘길 경우 유효하지 않은 경로이므로 continue
            if next_kaka > 1000 or next_bebe > 1000:
                continue

            if next_kaka >= nsk and next_bebe >= nsb:
                continue
            elif next_kaka <= nsk and next_bebe <= nsb:
                shortest[nxt] = (next_kaka, next_bebe)

            # next_kaka 에 대한 next_bebe 의 값이 최솟값이 아닐 경우 continue
            if next_bebe >= dp[nxt][next_kaka]:
                continue

            # 최솟값을 갱신
            dp[nxt][next_kaka] = next_bebe

            # 다음 노드가 최종 노드가 아니라면 큐에 삽입
            if nxt != n - 1:
                heappush(q, (next_kaka, next_bebe, nxt))

    # 마지막 노드에 도달했을 때의 각 kaka 수 별 최소 bebe 값을 곱한 값 중 최솟값을 구함
    result = min([kaka * dp[-1][kaka] for kaka in range(1, 1001)])

    return result if result != INF else -1
