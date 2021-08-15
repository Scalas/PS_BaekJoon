import sys

input = sys.stdin.readline


# 1629 곱셈
# a의 b승을 c로 나눈 나머지를 구하는 문제
# 단순한 문제지만 a, b, c의 값이 매우 크기때문에 단순히 연산자를 사용한 계산은 시간초과가 발생함
# 재귀를 사용한 분할정복으로 풀 수 있음
def sol1629():
    a, b, mod = map(int, input().split())

    def pow(a, b):
        nonlocal mod
        # b가 1일경우 a를 반환
        if b == 1:
            return a % mod

        # a의 b//2 제곱의 제곱을 구한 뒤 % mod
        res = pow(a, b // 2) ** 2 % mod

        # 만약 b가 홀수라면 a를 한번 더 곱한 뒤 % mod
        if b % 2:
            res = (res * a) % mod

        return res

    return pow(a, b)
