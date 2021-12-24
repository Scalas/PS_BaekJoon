import sys

input = sys.stdin.readline


# 2624 동전 바꿔주기
# 가진 동전의 금액과 갯수가 주어졌을 때 금액이 T인 지폐를 동전으로 바꿔줄 수 있는 모든 방법의 수를 구하는 문제
def sol2624():
    t = int(input())
    k = int(input())
    money = [0] * (t+1)
    money[0] = 1
    for _ in range(k):
        u, v = map(int, input().split())
        val = 0
        nmoney = money[:]
        for _ in range(v):
            val += u
            for i in range(t-val+1):
                nmoney[i + val] += money[i]
        money = nmoney
    return money[-1]
