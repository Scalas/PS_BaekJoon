import sys

input = sys.stdin.readline
INF = 10 ** 9


# 14863 서울에서 경산까지
# 출발지에서 목적지까지 각 구간마다 도보, 자전거로 갈때 걸리는 시간과 얻을 수 있는 모금비가 주어졌을 때
# 정해진 시간내에 목적지에 도착했을 때 얻을 수 있는 최대 모금비를 구하는 문제
def sol14863():
    n, k = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1] * (k+1) for _ in range(n)]

    # 현재 지나야할 구간이 cur번째 구간이고 time만큼의 시간이 지났을 때
    # 앞으로 얻을 수 있는 최대 모금비
    def dfs(cur, time):
        if cur == n:
            return 0

        if dp[cur][time] == -1:
            # 제시간에 도착할 수 없게되는 시점에서 얻을 수 있는 비용은 -INF
            res = -INF
            if time + info[cur][0] <= k:
                res = max(res, info[cur][1] + dfs(cur+1, time+info[cur][0]))
            if time + info[cur][2] <= k:
                res = max(res, info[cur][3] + dfs(cur+1, time+info[cur][2]))
            dp[cur][time] = res
        return dp[cur][time]

    # 처음 출발시점에서 앞으로 얻을 수 있는 최대비용 반환
    return dfs(0, 0)
