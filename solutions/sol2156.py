import sys

input = sys.stdin.read


# 2156 포도주 시식
# 포도주를 연속으로 세잔을 마실수 없을 때 n잔의 포도주가 주어지면 마실 수 있는 포도주의 최댓값을 구하는 문제
# 2579 계단오르기 문제와 거의 유사하다
# 다만 마지막 계단을 밟아야했던 2579번과 달리 마지막 와인을 마실 필요가 없기에 이전의 최댓값과도 비교가 필요하다
def sol2156():
    wines = [*map(int, input().split())]
    n, wines[0] = wines[0], 0
    if n < 3:
        print(sum(wines[:(n+1)]))
        return
    dp = [0] * (n + 1)
    dp[1] = wines[1]
    dp[2] = wines[1] + wines[2]
    for i in range(3, n + 1):
        dp[i] = max(dp[i-1], dp[i - 2] + wines[i], dp[i - 3] + wines[i - 1] + wines[i])
    print(max(dp))
