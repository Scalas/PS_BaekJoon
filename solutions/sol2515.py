import sys
from bisect import bisect_left

sys.setrecursionlimit(300000)
input = sys.stdin.readline


# 2515 전시장
# n개의 그림의 높이와 가격이 주어지고 그림들을 임의의 순서대로 일렬로 배치했을 때
# 눈에 보이는부분의 길이가 s 이상인 그림의 가격의 합의 최댓값을 구하는 문제
def sol2515():
    n, s = map(int, input().split())
    # 그림의 높이와 가격 목록을 높이기준 오름차순정렬
    # 중복되는 높이라면 가장 가격이 높은 것을 저장
    paints = dict()
    for _ in range(n):
        h, c = map(int, input().split())
        paints[h] = max(paints.get(h, 0), c)
    heights = sorted(paints.keys())
    hc = len(heights)

    # dp[i] 는 현재 배치된 그림중 가장 높은 것이 i 번째 그림일 때
    # 남은 그림을 배치하여 얻을 수 있는 가격의 합의 최댓값
    dp = [-1] * hc

    def dfs(cur):
        # 더이상 배치할 그림이 없을 경우
        if cur >= hc:
            return 0

        if dp[cur] < 0:
            res = 0
            curh = heights[cur]

            # 현재 그림을 배치할 경우
            nxt = bisect_left(heights, curh+s)
            res = max(res, dfs(nxt) + paints[curh])

            # 배치하지 않는 경우
            res = max(res, dfs(cur+1))

            dp[cur] = res

        return dp[cur]

    # 처음으로 높이가 s보다 큰 그림을 찾아 첫 인덱스로 사용
    for i in range(hc):
        if heights[i] >= s:
            return dfs(i)
