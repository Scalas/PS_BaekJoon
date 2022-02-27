import sys

input = sys.stdin.readline
INF = 10 ** 9


# 2300 기지국
# 2차원 평면 좌표상에 건물들의 좌표가 주어지고 x축에 기지국을 설치하여 모든 건물을 통신범위에 포함시키려한다
# 기지국은 설치된 위치를 중심으로 정사각형 범위안의 건물을 통신범위에 포함시킬 수 있다.
# 모든 건물을 포함시키도록 기지국을 지었을 때 기지국의 통신폭(정사각형 범위의 한 변의 길이)의 합의 최솟값을 구하는 문제
def sol2300():
    n = int(input())
    pos = [list(map(int, input().split())) for _ in range(n)]

    # 좌표기준 오름차순 정렬
    pos.sort()

    # dp[i] 는 i 까지의 건물을 통신범위에 포함시켰을 때 필요한 통신폭의 합의 최솟값
    dp = [0] * n

    # 0번 건물부터 마지막 건물을 하나의 기지국으로 통신범위에 포함시킬 때의 통신폭의 합
    x, y = pos[0]
    l, r, h = x, x, abs(y)
    for i in range(n):
        cx, cy = pos[i]
        r = cx
        h = max(h, abs(cy))
        dp[i] = max(r-l, h*2)

    for i in range(1, n):
        ndp = [dp[i-1]] * n
        x, y = pos[i]
        l, r, h = x, x, abs(y)
        # i번 부터 j번 까지의 건물을 하나의 기지국으로 통신범위에 포함시킬때의 통신폭의 합의 최댓값
        for j in range(i, n):
            cx, cy = pos[j]
            r = cx
            h = max(h, abs(cy))
            ndp[j] += max(r-l, h*2)

        # ndp 값으로 dp 값을 갱신
        for i in range(n):
            dp[i] = min(dp[i], ndp[i])

    # 마지막 건물까지 통신범위에 포함시키 위한 통신폭의 합의 최솟값
    return dp[-1]
