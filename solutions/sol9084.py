import sys

input = sys.stdin.readline


# 9084 동전
# 주어진 동전을 사용해서 특정 금액을 만드는 경우의 수를 구하는 문제
# 단순히 현재 금액에서 동전을 종류별로 더하여 나오는 금액의 경우의 수를
# 1씩늘리는 방식으로 점화식을 세우면 순서만 다르고 중복되는 경우의 수를 걸러낼 수 없음
# 각 동전을 사용한 경우의 수를 모두 구해둔 뒤 다음 동전을 더해나가는 방식을 사용해야함
def sol9084():
    answer = []
    for _ in range(int(input())):
        n = int(input())
        coins = list(map(int, input().split()))
        cost = int(input())
        dp = [0] * (cost+1)

        # 동전이 하나도 더해지지 않은 상태 - 금액 0
        dp[0] = 1

        # 동전이 더해질 때 마다
        for coin in coins:
            # coin까지 합하여 금액 i를 만들 수 있는 경우의 수는
            # coin 을 더하기 전에 금액 i-coin 을 만들었던 경우의 수와 coin을 만들었던 경우의 수를 합한 것과 같다.
            for i in range(coin, cost+1):
                dp[i] += dp[i-coin]
        answer.append(dp[-1])
    return '\n'.join(map(str, answer))
