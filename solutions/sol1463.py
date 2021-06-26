import sys

input = sys.stdin.readline


# 1463 1로 만들기
# 3으로 나누어떨어지면 3으로 나눈다, 2로 나누어떨어지면 2로 나눈다, 1을 뺀다
# 위 세가지 연산을 사용하여 정수 n을 1로 만드는데 필요한 연산의 최소횟수를 구하는 문제


# 첫 번째 시도
# 어떤 수 n을 만들 방법
# n//3 에서 3을 곱한 뒤 n%3 만큼 1을 더해주기
# n//2 에서 2를 곱한 뒤 n%2 만큼 1을 더해주기
# bottom up으로 n번째 dp까지 구하여 해결
def sol1463():
    n = int(input())
    if n == 1:
        print(0)
        return
    if n <= 3:
        print(1)
        return
    dp = [0] * (n + 1)
    dp[2] = dp[3] = 1
    for i in range(4, n + 1):
        dp[i] = 1 + min(dp[i // 3] + i % 3, dp[i // 2] + i % 2)
    print(dp[n])


# 두 번째 시도
# 재귀의 형태로 구성하여 연산 횟수를 줄임
dp = {1: 0, 2: 1, 3: 1}


def sol1463_2():
    n = int(input())
    print(make1(n))


def make1(num):
    if dp.get(num) == None:
        dp[num] = 1 + min(make1(num // 3) + num % 3, make1(num // 2) + num % 2)
    return dp[num]
