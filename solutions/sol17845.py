import sys

input = sys.stdin.readline


# 17845 수강 과목
# 각 과목의 공부시간과 중요도가 주어졌을 때 최대 공부시간 n을 넘지 않으면서
# 얻을 수 있는 수강한 강의의 중요도 합의 최댓값을 구하는 문제
def sol17845():
    n, k = map(int, input().split())
    dp = {0: 0}
    for _ in range(k):
        u, v = map(int, input().split())
        udp = {0: 0}
        for t, i in dp.items():
            ni, nt = i + u, t + v
            if nt > n:
                continue
            udp[nt] = max(dp.get(nt, 0), udp.get(nt, 0), ni)
        dp.update(udp)
    return max(dp.values())
