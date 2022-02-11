import sys

input = sys.stdin.readline
INF = 10 ** 9


# 12026 BOJ 거리
# 이동마다 이동하는 칸의 제곱만큼의 에너지가 필요하고
# n칸으로 이루어진 거리를 B O J 순으로 밟아가며 시작부터 마지막 위치까지 이동하려할 때
# 이동에 필요한 총 에너지의 최솟값을 구하는문제
def sol12026():
    n = int(input())
    road = input().rstrip()
    sq = [x ** 2 for x in range(n)]
    check = {'B': 'J', 'O': 'B', 'J': 'O'}
    dp = [INF] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if road[j] == check[road[i]]:
                dp[i] = min(dp[i], dp[j] + sq[i-j])
    return dp[-1] if dp[-1] != INF else -1
