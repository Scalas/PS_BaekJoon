import sys


# 11047 동전 0
# 최대한 적은 동전으로 특정 금액을 만들려면 금액이 큰 동전을 많이 쓸수록 좋다
# 동전의 단위에 1이 있어 자연수의 금액은 무조건 만들 수 있기 때문에
# 단순히 큰 동전을 최대한 사용하고 다음으로 큰 동전으로 같은 연산을 반복하여 풀 수 있다 (그리디)
def sol11047():
    n, k, *coins = map(int, sys.stdin.read().split())
    answer = 0
    for i in range(n - 1, -1, -1):
        coin, cnt = coins[i], k // coins[i]
        answer += cnt
        k -= coin * cnt
    print(answer)
