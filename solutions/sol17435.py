import sys
from math import log2, ceil

input = sys.stdin.readline


# 17435 합성함수와 쿼리
# 함수 f(x)의 값들이 주어졌을때, fn(x) 가 f(f(f(...f(x)...))) 와 같이 함수 f를 n중첩한 결과라고 한다.
# 이 때, 주어진 m개의 n, x 쌍에 대해 fn(x) 를 각각 구하는 문제
# LCA 문제는 아니지만 LCA 알고리즘의 핵심인 sparse table 을 응용해서 풀 수 있는 문제이다.
def sol17435():
    # 주어진 함수값의 수
    m = int(input())

    # 500000 <= 2^k
    k = ceil(log2(500000))

    # sparse table :  f[x][k] = fk(x)
    f = [[-1] * k for _ in range(m + 1)]
    fn = list(map(int, input().split()))
    for i in range(m):
        f[i + 1][0] = fn[i]

    # 점화식 f[i][j] = f[f[i][j-1]][j-1] 에 따라 sparse table 나머지 채우기
    for j in range(1, k):
        for i in range(1, m + 1):
            f[i][j] = f[f[i][j - 1]][j - 1]

    # 쿼리의 수
    q = int(input())

    # 각 쿼리의 정답 구하기
    answer = []
    for _ in range(q):
        # 함수 중첩수 n, 인자값 x
        n, x = map(int, input().split())

        # 중첩수가 0이 되면 종료
        while n:
            # f[x][d] == f2^d(x)
            d = int(log2(n))
            x = f[x][d]

            # 2^d 중첩만큼 처리했기 때문에 남은 중첩수에서 감산
            n -= (1 << d)

        # 정답리스트에 쿼리의 정답 저장
        answer.append(x)

    # 출력 형식에 맞춰 정답 리스트 반환
    return '\n'.join(map(str, answer))
