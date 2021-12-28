import sys

input = sys.stdin.readline
INF = 10 ** 9


# 13302 리조트
# 하루 이용권 / 10,000원 / 쿠폰 0개
# 연속 3일권 / 25,000원 / 쿠폰 1개
# 연속 5일권 / 37,000원 / 쿠폰 2개
# 리조트의 이용권의 가격과 지급되는 쿠폰 수가 위와 같을 때
# n일 중 주어진 m개의 날을 제외한 모든 날에 리조트를 사용하기 위해
# 필요한 최소 비용을 구하는 문제
def sol13302():
    ticket = [(1, 10000), (3, 25000), (5, 37000)]
    n, m = map(int, input().split())

    # resort[day] 가 참이라면 그 날에는 리조트를 사용할 수 없음
    resort = [False] * (n+1)
    for day in map(int, input().split()):
        resort[day] = True

    # dp[i][j] 는 현재 i일째이고 j개의 쿠폰을 가졌을때
    # 남은 일수만큼 리조트를 이용하기 위한 최소비용
    dp = [[0] * 40 for _ in range(n+1)]

    def dfs(day, coupon):
        # 리조트에 갈 수 없는 날인 경우 갈 수 있는 날까지 스킵
        while day <= n and resort[day]:
            day += 1

        # n일을 넘어갔을 경우 리조트 이용이 완료
        if day > n:
            return 0

        # 아직 계산되지 않은 상태인 경우
        if not dp[day][coupon]:
            res = INF

            # 하루, 3일, 5일중 한가지 이용권을 선택하여 구매
            for t in range(3):
                d, c = ticket[t]
                res = min(res, dfs(day+d, coupon + t) + c)

            # 쿠폰이 3개 이상이라면 쿠폰을 사용하는 경우도 탐색
            if coupon >= 3:
                res = min(res, dfs(day+1, coupon - 3))

            # 결과값 저장
            dp[day][coupon] = res

        # i일째 쿠폰이 j개일 때 앞으로 필요한 최소비용을 반환
        return dp[day][coupon]

    return dfs(1, 0)
