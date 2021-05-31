import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


# 1629 곱셈
# a의 b승을 c로 나눈 나머지를 구하는 문제
# 단순한 문제지만 a, b, c의 값이 매우 크기때문에 단순히 연산자를 사용한 계산은 시간초가가 발생함
# 재귀를 사용한 분할정복으로 풀 수 있음
def sol1629():
    a, b, c = map(int, input().split())
    print(mult(a, b, c))


def mult(a, b, c):
    # b가 1이하일 경우 a의 b승을 c로 나눈 값을 반환
    if (b <= 1):
        return a ** b % c

    # b를 2로 나누어 재귀호출한 뒤 그 결과를 제곱하고 c로 나눈 값을 반환
    # b가 홀수일 경우 제곱한 값에 a를 한번 더 곱한 뒤 c로 나눈다
    m = b // 2
    if (b % 2 == 0):
        return mult(a, m, c) ** 2 % c
    else:
        return mult(a, m, c) ** 2 * a % c
