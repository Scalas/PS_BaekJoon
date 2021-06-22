import sys

input = sys.stdin.read


# 11050 이항계수 c(n, k)를 구하는 문제
# 1 <= n <= 10,  0 <= k <= n 으로 범위가 매우 작기에
# 단순히 이항계수의 정의에 따라 ( n * (n-1) * ... * (n-k+1) ) // ( 1 * 2 * ... * k ) 을 계산하여 구할 수 있다
def sol11050():
    n, k = map(int, input().split())
    top, bot = 1, 1
    for num in range(1, k+1):
        top *= (n-num+1)
        bot *= num

    print(top//bot)
