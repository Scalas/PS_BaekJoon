import sys

input = sys.stdin.read


# 15486 퇴사 2
# 1일부터 n일까지 소요일수와 완료시 얻을 수 있는 금액으로 이루어진 상담예정 리스트가 주어지고
# n+1일째에는 퇴사를 해야할 경우 퇴사 전까지 얻을 수 있는 최대 수익을 구하는 문제
def sol15486():
    n, *cand = map(int, input().split())

    # dp[i] 는 i일부터 퇴사전까지 얻을 수 있는 최대 수익
    dp = [0] * (n+2)

    # dp[n]은 마지막날의 상담예정이 하루짜리 상담이라면 해당 상담의 수익이 된다
    if cand[-2] == 1:
        dp[n] = cand[-1]

    # i일 째의 수익은 그날의 상담을 하지 않고 다음날로 넘어간 경우의 수익과
    # 그날의 상담을 하고 상담이 끝나는 다음날로 넘어간 경우의 수익중 최댓값이 된다.
    for i in range(n-1, 0, -1):
        idx = 2 * (i - 1)
        d, v = cand[idx], cand[idx+1]
        dp[i] = dp[i+1]
        if i+d-1 <= n:
            dp[i] = max(dp[i], dp[i+d]+v)
    return dp[1]
