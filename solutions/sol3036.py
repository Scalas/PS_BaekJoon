import sys

input = sys.stdin.read


# 3036 링
# 서로 접한 링들의 길이가 주어졌을 때
# 첫 링이 한바퀴 돌아가면 나머지 링이 돌아가는 바퀴 수를 기약분수의 형태로 구하는 문제
# 각 링의 길이에 대해 첫 링의 길이와의 최대공약수를 구하면 해결 가능하다
def sol3036():
    n, f, *rings = map(int, input().split())
    answer = []
    for ring in rings:
        g = gcd(f, ring)
        answer.append(f'{f // g}/{ring // g}')
    print('\n'.join(answer))


def gcd(n, m):
    if n < m:
        n, m = m, n
    while m != 0:
        n, m = m, n % m
    return n

    sol3036()