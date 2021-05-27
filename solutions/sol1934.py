import sys

input = sys.stdin.readline
out = sys.stdout.write


def gcd(a, b):
    r = a % b
    if (r == 0):
        return b
    else:
        return gcd(b, r)


def sol1934():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if (a < b):
            a, b = b, a

        answer = a * b // gcd(a, b)
        out(f'{answer}\n')


sol1934()