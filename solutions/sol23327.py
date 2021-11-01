import sys

input = sys.stdin.readline


# 23327 리그전 오브 레전드 모두 더한 값
# 수열이 주어졌을 때 특정 구간의 수 중 2개를 뽑아 서로 곱한 값의 합을 구하는 문제
# 구간합과 동적계획법을 사용하여 해결 가능하다.
def sol23327():
    n, q = map(int, input().split())
    power = [0, *map(int, input().split())]
    acc = [0] * (n+1)
    dp = [0] * (n+1)
    for i in range(1, n+1):
        acc[i] = acc[i-1] + power[i]
        dp[i] = dp[i-1] + acc[i-1] * power[i]

    answer = []
    for _ in range(q):
        l, r = map(int, input().split())
        answer.append(dp[r] - dp[l-1] - (acc[r]-acc[l-1]) * acc[l-1])

    return '\n'.join(map(str, answer))

