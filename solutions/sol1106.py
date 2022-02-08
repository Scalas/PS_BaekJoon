import sys

input = sys.stdin.readline
INF = 10 ** 5


# 1106 호텔
# 각 도시에서 한번 홍보를 하는데 드는 비용과 그 때마다 유치할 수 있는 고객의 수가 주어질 때
# 최소 c명의 고객을 유치하기 위해 필요한 비용의 최솟값을 구하는 문제
def sol1106():
    c, n = map(int, input().split())

    # dp[i] 는 i 명의 고객을 유치하기 위해 필요한 최소비용
    # 한번의 홍보로 유치할 수 있는 고객의 수가 최대 100명이므로
    # 한번의 홍보로 고객의 수가 c명 미만에서 c명을 넘어서는 경우는 최대 c+99 까지 (c-1 + 100)
    dp = [INF] * (c+100)

    # 주어진 홍보 효율로 dp 갱신
    dp[0] = 0
    for _ in range(n):
        u, v = map(int, input().split())
        dp[v] = min(dp[v], u)

    # dp[i] = min(dp[0] + dp[i], dp[1] + dp[i-1], ... , dp[j] + dp[i-j])
    # j는 i // 2 까지만 검사해도 됨 (그 이후는 대칭)
    for i in range(1, c+100):
        for j in range(i // 2 + 1):
            dp[i] = min(dp[i], dp[j] + dp[i-j])

    return min(dp[c:])
