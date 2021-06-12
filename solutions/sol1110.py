import sys


def sol1110():
    n = int(sys.stdin.readline())
    num = func(n)
    answer = 1
    while num!=n:
        num = func(num)
        answer += 1
    print(answer)


def func(n):
    m = n % 10
    d = n // 10
    return (m * 10) + ((d + m) % 10)
