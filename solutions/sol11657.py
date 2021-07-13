import sys

input = sys.stdin.readline
INF = float('inf')


# 11657 타임머신
# 음수간선이 포함된 그래프의 최단거리 구하기
# 벨만포드 알고리즘을 사용하여 풀 수 있다
def sol11657():
    n, m = map(int, input().split())
    edge = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge.append((a - 1, b - 1, c))

    dp = [INF] * n
    dp[0] = 0
    for v in range(n - 1):
        check = True
        for s, e, t in edge:
            if dp[s] + t < dp[e]:
                dp[e] = dp[s] + t
                check = False
        if check:
            break

    check = False
    for s, e, t in edge:
        if dp[s] + t < dp[e]:
            check = True
            break
    print(-1 if check else '\n'.join(map(conv, dp[1:])))


def conv(num):
    return '-1' if num == INF else str(num)
