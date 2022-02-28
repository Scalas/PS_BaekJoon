import sys

input = sys.stdin.readline
INF = float('inf')


# 1727 커플 만들기
# n명의 남자와 m명의 여자의 성격치가 양의 정수로 주어지고
# 최대한 많은 커플을 만들어야 할 때 그 커플들의 성격 차의 합의 최솟값을 구하는 문제
def sol1727():
    n, m = map(int, input().split())

    # 두 그룹중 수가 적은쪽이 a, 많은쪽이 b가 되도록 한다
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    if n > m:
        n, m = m, n
        a, b = b, a

    # a와 b를 오름차순 정렬
    a.sort()
    b.sort()

    # dp의 초기값은 a 그룹의 0번째 사람이 b 그룹의 i번째 까지의 사람중에 짝을 골랐을 때 성격 차의 합의 최솟값
    dp = [0] * m
    dp[0] = abs(a[0] - b[0])
    for i in range(1, m):
        dp[i] = min(dp[i-1], abs(a[0] - b[i]))

    for i in range(1, n):
        # a 그룹의 i번째 사람이 b 그룹의 j번째 까지의 사람중에 짝을 고를 경우 성격 차의 합의 최솟값
        ndp = [INF] * m

        # 1. j번째 사람을 짝으로 고르는 경우
        # 2. j-1번째 까지의 사람중에 짝을 고르는 경우
        # 위 두 가지 경우중 성격 차의 합의 최솟값이 ndp[j]가 됨
        for j in range(i, m):
            ndp[j] = min(ndp[j-1], abs(a[i] - b[j]) + dp[j-1])

        # ndp 값으로 dp 갱신
        dp = ndp

    # a 그룹의 마지막 사람까지 짝을 선택했을 때 성격 차의 합의 최솟값 반환
    return min(dp)
