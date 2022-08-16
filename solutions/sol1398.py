import sys

input = sys.stdin.readline


# 1398 동전 문제
# 10 ^ k, 25 * 100 ^ k 의 동전들을 최소한으로 사용하여 주어진 금액을 만들 때
# 필요한 동전의 최소 갯수를 구하는 문제
def sol1398():
    # 동전들의 관계가 배수관계가 아니기 때문에 큰 수부터 넣는게 반드시 정답이 아닐 수 있음
    # 예를들어 30의 경우 25를 먼저 넣고나면 1원짜리 5개를 추가하여 6개가 필요한데,
    # 10원짜리로만 채울 경우 3개면 충분하다.
    # 그러나 이 문제에서 금액은 최대 10 ^ 15이므로 dp를 사용한 풀이도 어렵다

    # 동전의 금액은 [1, 10, 25] -> [100, 1000, 2500] 과 같이 이루어지므로
    # 100의자리 이상의 금액을 만들 경우, 1, 10, 25를 사용하는 것은 항상
    # 100, 1000, 2500을 사용하는 것 보다 비효율적이며
    # 10000의 자리 이상의 금액이라면 100, 1000, 2500을 사용하는 것은 항상
    # 10000, 100000, 250000 을 사용하는 것 보다 비효율적이다.
    # 그러므로 100 미만의 수를 1, 10, 25로 만들기 위한 동전의 최소 갯수를 dp로 구한 뒤
    # 모든 동전을 두자리씩 끊어서 필요한 동전의 갯수를 구해나가는 방법으로 이 문제를 풀 수 있다.
    dp = [0] * 100
    coins = [25, 10, 1]
    for i in range(1, 100):
        res = i
        for coin in coins:
            if i >= coin:
                res = min(res, dp[i - coin] + 1)
        dp[i] = res

    answer = []
    for _ in range(int(input())):
        n = int(input())
        res = 0
        while n:
            res += dp[n % 100]
            n //= 100
        answer.append(res)
    return '\n'.join(map(str, answer))