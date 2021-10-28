import sys

input = sys.stdin.readline


# 16194 카드 구매 2
# 가장 적은 비용으로 정해진 갯수만큼의 카드를 구매할 때의 비용을 구하는 문제
def sol16194():
    n = int(input())
    cost = [0, *map(int, input().split())]
    for i in range(2, n+1):
        cost[i] = min([cost[j] + cost[i-j] for j in range(i//2+1)])
    return cost[n]
