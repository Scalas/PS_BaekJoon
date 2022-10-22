import sys

input = sys.stdin.readline


# 1633 최고의 팀 만들기
# 각 선수들의 백 능력치와 흑 능력치가 주어지고
# 그 중 15명의 백 선수와 15명의 흑 선수 총 30명의 선수를 뽑아
# 흑백 능력치의 합이 최대가 되는 팀을 만들 때, 그 팀의 능력치의 합을 구하는 문제
def sol1633():
    players = []
    while True:
        inp = list(map(int, input().split()))
        if not inp:
            break
        players.append(inp)
    n = len(players)

    dp = [[[0] * 16 for _ in range(16)] for _ in range(n)]

    def dfs(cur, cw, cb):
        if cur == n:
            return 0

        if not dp[cur][cw][cb]:
            res = 0

            need = 30 - cw - cb
            if n - cur - need > 0:
                res = max(res, dfs(cur + 1, cw, cb))

            if cw < 15:
                res = max(res, dfs(cur + 1, cw + 1, cb) + players[cur][0])

            if cb < 15:
                res = max(res, dfs(cur + 1, cw, cb + 1) + players[cur][1])
            dp[cur][cw][cb] = res

        return dp[cur][cw][cb]

    return dfs(0, 0, 0)
