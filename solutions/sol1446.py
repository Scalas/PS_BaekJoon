import sys

input = sys.stdin.readline


# 1446 지름길
# 시작위치, 도착위치, 거리 로 이루어진 n개의 지름길이 주어졌을 때
# 위치 d까지 이동하기 위한 최소 이동거리를 구하는 문제
def sol1446():
    n, d = map(int, input().split())

    # dp[i] 는 i까지 가기 위한 최단거리
    dp = [i for i in range(d+1)]

    # 지름길의 리스트를 도착위치 -> 이동거리 기준으로 오름차순정렬
    short_cut = [list(map(int, input().split())) for _ in range(n)]
    short_cut.sort(key=lambda x: (x[1], x[2]))

    for s, e, dst in short_cut:
        # 목적지가 고속도로의 길이보다 클 경우 종료
        if e > d:
            break

        # e로 가는 더 빠른 길을 찾았을 경우
        if dp[s] + dst < dp[e]:
            dp[e] = dp[s] + dst
            for i in range(e+1, d+1):
                dp[i] = dp[i-1] + 1

    # 고속도로의 마지막 위치에 도달하는데 필요한 최소 이동거리
    return dp[-1]
