import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float('inf')


# 1238 파티
# 1부터 n까지의 마을에 살고있는 1~n번의 학생들이 x번 마을에 모여서 파티를 한 후 다시 자신의 마을로 돌아가려한다
# 학생들이 x번 마을에 모이고 다시 돌아가는데 가장 시간이 적게 걸리는 경로를 통해 간다고 할 때
# 학생들이 파티를 위해 모이는데 걸린시간과 마을로 돌아가는데 걸린시간의 합중 최댓값을 구하는 문제
def sol1238():
    n, m, x = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))

    tox = [0] * (n+1)
    # 1번부터 n번학생까지 x로 가는 최단거리를 더함
    for i in range(1, n+1):
        dp = [INF] * (n+1)
        dp[i] = 0
        q = [(0, i)]
        while q:
            dst, mid = heappop(q)
            if dp[mid] < dst:
                continue

            for nxt, dist in g[mid]:
                ndst = dst + dist
                if ndst < dp[nxt]:
                    dp[nxt] = ndst
                    heappush(q, (ndst, nxt))
        tox[i] += dp[x]

        # 만약 x번 학생이라면 dp배열은 학생들이 파티를 마치고 돌아가는데 걸리는 최단시간이 됨
        if i == x:
            for j in range(1, n+1):
                tox[j] += dp[j]

    # 걸린 시간중 최댓값 반환
    return max(tox)

