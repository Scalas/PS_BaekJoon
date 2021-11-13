import sys

input = sys.stdin.readline


# 1562 계단 수
# 0으로 시작하지 않으며 인접한 자릿수끼리의 차가 1인 수를 계단수라고 할 때
# 0~9의 수를 모두 포함한 n 자리의 계단수의 갯수를 구하는 문제
def sol1562():
    n = int(input())
    mod = 1000000000

    # 0~9까지의 수의 포함여부를 비트마스크로 관리
    # dp[i][j][k] 는 현재 자릿수가 i이고 n자리 수가 되기위해 j개의 자릿수를 더해야하며
    # 0~9까지의 수의 포함여부가 k(비트마스크)일 때 만들 수 있는 0~9를 모두 포함하는 n자리 계단수의 갯수
    full_visit = 2 ** 10 - 1
    dp = [[[-1] * (full_visit+1) for _ in range(n)] for _ in range(10)]

    # 0~9까지의 수를 모두 포함하고 n자리인 수의 dp값을 1로
    # 0~9까지의 수를 모두 포함하지 않고 n자리인 수의 dp값을 0으로 초기화
    for i in range(10):
        dp[i][0][full_visit] = 1
        for j in range(full_visit):
            dp[i][0][j] = 0

    # 현재 자릿수보다 1 큰 수를 붙이거나 1 작은수를 붙이는 두 가지 경우의 수를 더하여
    # 현재 상태에서 만들 수 있는 계단수의 갯수를 구할 수 있음
    # 단, 현재 자릿수가 0이면 작은 수는 붙일 수 없으며 9이면 큰 수를 붙일 수 없다.
    def dfs(cur, rem, visited):
        if dp[cur][rem][visited] < 0:
            res = 0
            if cur:
                res = (res + dfs(cur-1, rem-1, visited | (1 << (cur-1))))
            if cur < 9:
                res = (res + dfs(cur+1, rem-1, visited | (1 << (cur+1))))
            dp[cur][rem][visited] = res
        return dp[cur][rem][visited]

    # 1~9로 시작하며 0~9를 모두 포함하는 계단수의 갯수를 모두 더한 뒤 mod로 나눈 나머지를 반환
    return sum([dfs(i, n-1, 1 << i) for i in range(1, 10)]) % mod
