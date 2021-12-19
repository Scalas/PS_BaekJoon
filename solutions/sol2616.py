import sys

input = sys.stdin.readline


# 2616 소형기관차
# m개의 연속한 객차를 끌수있는 소형기관차 3개로 n개의 객차를 나눠 끌 때
# 태울 수 있는 최대 승객 수를 구하는 문제
def sol2616():
    n = int(input())
    train = list(map(int, input().split()))
    m = int(input())

    for i in range(n-1):
        train[i+1] += train[i]
    train.append(0)

    dp = [0] * (n + 1)
    for _ in range(3):
        ndp = [0] * (n + 1)
        for i in range(n-m+1):
            ndp[i+m-1] = max(ndp[i+m-2], dp[i-1] + train[i+m-1] - train[i-1])
        dp = ndp
    return dp[-2]
