import sys

input = sys.stdin.readline


# 16493 최대 페이지 수
# m개의 챕터를 구성하는 페이지 수와 읽는데 걸리는 일수가 주어지고
# 남은 일수가 주어졌을 때, 남은 일수동안 읽을 수 있는 최대 페이지 수를 구하는 문제
# 단, 챕터를 읽으려면 끝까지 읽어야한다.
def sol16493():
    n, m = map(int, input().split())
    dp = {0: 0}
    for _ in range(m):
        w, v = map(int, input().split())
        udp = {}
        for weight, value in dp.items():
            nw, nv = weight + w, value + v
            if nw <= n:
                udp[nw] = max(dp.get(nw, 0), udp.get(nw, 0), nv)
        dp.update(udp)

    return max(dp.values())
