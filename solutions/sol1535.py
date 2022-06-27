import sys

input = sys.stdin.readline


# 1535 안녕
# n명의 사람에게 인사할때마다 일정량의 체력을 잃고 일정량의 기쁨을 얻을 때
# 체력 소모가 100 이상이 되지 않으면서 얻을 수 있는 최대의 기쁨을 구하는 문제
def sol1535():
    n = int(input())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    dp = [[-1] * 100 for _ in range(n)]

    def dfs(cur, hp):
        if cur == n:
            return 0

        if dp[cur][hp] < 0:
            res = dfs(cur + 1, hp)
            if u[cur] < 100 - hp:
                res = max(res, dfs(cur + 1, hp + u[cur]) + v[cur])
            dp[cur][hp] = res

        return dp[cur][hp]

    return dfs(0, 0)
