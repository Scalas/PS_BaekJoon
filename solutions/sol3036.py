import sys

input = sys.stdin.readline


def gcd(a, b):
    r = a % b
    if (r == 0):
        return b
    else:
        return gcd(b, r)


def sol3036():
    input()
    rings = list(map(int, input().split()))
    answer = []
    for ring in rings[1:]:
        a, b = ring, rings[0]
        if (a < b):
            a, b = b, a
        g = gcd(a, b)
        answer.append(f'{rings[0] // g}/{ring // g}')

    print(*answer, sep='\n')


sol3036()