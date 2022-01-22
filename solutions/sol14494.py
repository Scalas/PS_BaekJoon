import sys

input = sys.stdin.readline
MOD = 1000000007


# 14494 다이나믹이 뭐에요?
# n * m 배열에서 오른쪽, 아래, 오른쪽아래 대각선의 세 방향으로만 이동할 수 있을 때
# (1, 1) 에서 (n, m)으로 이동하는 경우의 수를 구하는 문제
def sol14494():
    n, m = map(int, input().split())
    dp = [1] * m
    for _ in range(n-1):
        ndp = [0] * m
        ndp[0] = 1
        for i in range(1, m):
            ndp[i] = (dp[i] + ndp[i-1] + dp[i-1]) % MOD
        dp = ndp
    return dp[-1]
