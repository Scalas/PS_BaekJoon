import sys

input = sys.stdin.readline


# 2407 조합
# combination(n, m) 을 구하는 문제
# n 과 m이 굉장히 작기때문에 별도의 알고리즘이 필요하지 않음
def sol2407():
    n, m = map(int, input().split())

    # c(n, m) = c(n, n-m) 임을 이용하여
    # m 과 n-m 중 작은쪽을 m으로 하여 연산 횟수를 줄인다
    m = min(m, n - m)

    # c(n, m) = (n * ... * (n-m+1)) / (1 * ... * m) 임을 이용하여 조합을 구하여 반환
    u, v = 1, 1
    for i in range(m):
        u *= n - i
        v *= i + 1

    return u // v
