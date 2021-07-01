import sys

input = sys.stdin.readline
mod = 1000


# 10830 행렬 제곱
# 행렬 a를 b 제곱한 뒤 모든 요소를 1000으로 모듈러연산한 결과를 출력하는 문제
# 숫자 a의 b제곱 구하기와 사실상 같은 문제
# 행렬 곱셈만 구현해준 뒤 분할정복으로 접근하면 풀 수 있음
# 주의 : 행렬 a가 1000을 요소로 가지고 b가 1인 경우에 행렬의 곱 연산이 실행되지 않아
# 모듈러연산이 적용되지 않는 예외가 발생.  제곱연산 결과에 한번더 모듈러연산을 해줄 필요가 있음
def sol10830():
    n, b = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    answer = matsq(a, b)
    for i in range(n):
        for j in range(n):
            answer[i][j] %= 1000
    sys.stdout.write('\n'.join([' '.join(map(str, answer[i])) for i in range(n)]))


def matmult(a, b):
    global mod
    n = len(a[0])
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] += a[i][k] * b[k][j]
                ret[i][j] %= mod
    return ret


def matsq(a, b):
    if b == 1:
        return a
    ret = matsq(a, b // 2)
    ret = matmult(ret, ret)
    if b % 2 != 0:
        ret = matmult(ret, a)
    return ret
