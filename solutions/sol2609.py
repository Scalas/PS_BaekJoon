import sys

input = sys.stdin.readline
out = sys.stdout.write


def sol2609():
    a, b = map(int, input().split())
    h, l = a, b
    if (h < l):
        h, l = l, h
    r = h % l
    while (r != 0):
        h, l = l, r
        r = h % l
    gcd = l
    lcm = a * b // gcd
    print(gcd, lcm, sep='\n')