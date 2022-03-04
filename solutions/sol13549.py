import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float('inf')


# 13549 숨바꼭질 3
# 수빈이는 0초만에 현재위치 * 2 의 위치로 이동하거나 1초만에 현재위치 - 1 혹은 현재위치 + 1 위치로 이동 가능하다
# 수빈이가 n, 동생이 k 에 위치할 때 수빈이가 동생의 위치로 이동하기 위해 필요한 최소시간을 구하는 문제
def sol13549():
    n, k = map(int, input().split())

    # 동생이 수빈이와 같거나 뒤의 위치에 있는 경우
    if n >= k:
        return n-k

    # max_bound 까지 0초로 이동하더라도 k까지 되돌아가는데 걸리는 시간이
    # 그냥 걸어가는 시간보다 길다면 의미가 없기 때문에 max_bound 는 2 * k - n
    max_bound = 2 * k - n

    # 다익스트라 알고리즘으로 위치 n으로 부터의 최단거리 탐색
    dp = [INF] * max_bound

    # 초기위치 n
    q = [(0, n)]
    dp[n] = 0

    while q:
        dst, cur = heappop(q)

        if dp[cur] < dst:
            continue

        nxt = cur-1
        if nxt >= 0 and dst + 1 < dp[nxt]:
            dp[nxt] = dst + 1
            heappush(q, (dst+1, nxt))

        nxt = cur+1
        if nxt < max_bound and dst + 1 < dp[nxt]:
            dp[nxt] = dst + 1
            heappush(q, (dst+1, nxt))

        nxt = cur * 2
        if nxt < max_bound and dst < dp[nxt]:
            dp[nxt] = dst
            heappush(q, (dst, nxt))

    return dp[k]
