import sys

input = sys.stdin.readline


# 9613 GCD 합
# 주어진 수열의 가능한 모든 쌍에 대한 GCD를 합한 값을 구하는 문제
def sol9613():
    answer = []
    for t in range(int(input())):
        g = 0
        seq = list(map(int, input().split()))
        for i in range(1, len(seq) - 1):
            for j in range(i + 1, len(seq)):
                g += gcd(seq[i], seq[j])
        answer.append(g)
    return '\n'.join(map(str, answer))


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
