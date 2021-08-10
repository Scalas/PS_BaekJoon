import sys

input = sys.stdin.read


# 2981 검문
# n 개의 수를 m으로 나눠 그 나머지가 모두 같게 하는 m을 모두 구하는 문제
# n개의 수를 정렬한 뒤 인접한 수 끼리의 차들의 최대 공약수를 구하고, 그 최대 공약수의 약수를 구하는 방식으로 접근해야함
# A1 = a1 * m + r,  A2 = a2 * m + r
# A2 - A1 = (a2 - a1) * m
# 약수를 구할때는 최대공약수의 제곱근까지만 탐색, 나눈 m값과 몫이 모두 약수가 된다
# 1을 포함하지 않기때문에 최대공약수 자체도 따로 추가해줘야한다
def sol2981():
    n, *seq = map(int, input().split())
    g, *diff = [abs(seq[i] - seq[i - 1]) for i in range(1, n)]
    for d in diff:
        g = gcd(g, d)
    res = {g}
    for i in range(2, int(g**.5) + 1):
        if g % i == 0:
            res.add(i)
            res.add(g // i)
    return ' '.join(map(str, sorted(res)))


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
