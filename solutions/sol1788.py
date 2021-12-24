import sys

input = sys.stdin.readline


# 1788 피보나치 수의 확장
# 절댓값이 1000000 이하인 정수 n에 대해 피보나치 값을 구하는 문제
def sol1788():
    n = int(input())
    if n == 0:
        return '%d\n%d' % (0, 0)

    if n < 0:
        dp = [1, 0]
        for _ in range(-n):
            dp = [dp[-1], mod(dp[-2] - dp[-1])]
    else:
        dp = [0, 1]
        for _ in range(n-1):
            dp = [dp[-1], mod(dp[-1] + dp[-2])]
    sign = 1 if dp[-1] > 0 else 0 if dp[-1] == 0 else -1
    return '%d\n%d' % (sign, abs(dp[-1]))


def mod(n):
    sign = 0 if not n else 1 if n > 0 else -1
    return (abs(n) % 1000000000) * sign
