import sys
input = sys.stdin.readline


# 2662 기업 투자
# m개의 기업에 투자금 n만원을 분산투자하여 얻을 수 있는 최대 금액을 구하는 문제
def sol2662():
    n, m = map(int, input().split())

    # cost[i][j] 는 i만원을 j기업에 투자했을 때 얻을 수 있는 이익금
    cost = [[0] * m for _ in range(n+1)]
    for i in range(1, n+1):
        _, *profits = map(int, input().split())
        for j in range(m):
            cost[i][j] = profits[j]

    # dp[i][j] 는 남은 투자금이 i만원이고 현재 j기업에 투자할 금액을 고를 차례일 때
    # 앞으로 얻을 수 있는 최대 이익금
    dp = [[0] * m for _ in range(n+1)]

    # trace[i][j] 는 남은 투자금이 i만원이고 현재 j기업에 투자할 금액을 고를 차례일 때
    # 최대 이익금을 얻기 위해 j기업에 투자해야할 금액
    trace = [[0] * m for _ in range(n+1)]

    def dfs(inv, cur):
        # 투자금이 떨어졌거나 더이상 투자할 기업이 없다면 0 반환
        if not inv or cur == m:
            return 0

        # 투자금이 inv 만큼 남았고 cur번째 기업의 투자금을 정하는 중일 때
        # 앞으로 얻을 수 있는 최대이익 계산, 이때 얼마를 투자해야하는지 trace에 기록
        if not dp[inv][cur]:
            res = 0
            for amount in range(inv+1):
                cal = dfs(inv-amount, cur+1) + cost[amount][cur]
                if res < cal:
                    res = cal
                    trace[inv][cur] = amount
            dp[inv][cur] = res
        return dp[inv][cur]

    # 최대 이익
    max_profit = dfs(n, 0)

    # 최대 이익을 얻기 위해 필요한 각 기업에의 투자액수
    inv_list = [0] * m
    inv = n
    for corp in range(m):
        amount = trace[inv][corp]
        inv_list[corp] = amount
        inv -= amount

    return '\n'.join([str(max_profit), ' '.join(map(str, inv_list))])
