import sys

input = sys.stdin.readline


# 2056 작업
# 작업에 걸리는 시간과 필요한 선행작업 관계가 주어졌을 때
# 모든 작업을 마치는데 걸리는 최소시간을 구하는 문제
# 위상정렬을 사용해서 간단하게 해결 가능하다.
def sol2056():
    n = int(input())
    g = [[] for _ in range(n+1)]
    time = [0] * (n+1)
    degree = [0] * (n+1)
    q = []
    for i in range(1, n+1):
        info = list(map(int, input().split()))
        time[i] = info[0]
        degree[i] = info[1]
        for j in range(2, len(info)):
            g[info[j]].append(i)
        if not degree[i]:
            q.append(i)

    dp = [0] * (n+1)
    while q:
        nq = []
        for w in q:
            dp[w] += time[w]
            for nxt in g[w]:
                degree[nxt] -= 1
                dp[nxt] = max(dp[nxt], dp[w])
                if not degree[nxt]:
                    nq.append(nxt)
        q = nq

    return max(dp)
