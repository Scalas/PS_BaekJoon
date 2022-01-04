import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


# 1563 개근상
# 개근상을 받기 위해서는 지각은 최대 1번, 결석은 연속으로 2번까지만 허용된다
# 즉, 2번이상 지각하거나 3번이상 연속으로 결석할 경우 개근상을 받을 수 없다
# 학기 수가 n일일 때 개근상을 받을 수 있는 경우의 수를 구하는 문제
def sol1563():
    n = int(input())
    dp = [[[0] * 3 for _ in range(2)] for _ in range(n)]

    def dfs(day, late, absent):
        if day == n:
            return 1
        if not dp[day][late][absent]:
            res = 0

            # 출석하기
            res += dfs(day+1, late, 0)

            # 지각하기
            if not late:
                res += dfs(day+1, 1, 0)

            # 결석하기
            if absent < 2:
                res += dfs(day+1, late, absent+1)

            dp[day][late][absent] = res % 1000000
        return dp[day][late][absent]

    return dfs(0, 0, 0)
