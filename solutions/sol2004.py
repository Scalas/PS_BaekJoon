import sys

input = sys.stdin.readline


# 2004 조합 0의 갯수
# c(n, m)의 뒤에서부터 0이 아닌 숫자가 나올 때까지 0의 갯수를 구하는 문제


# 1676번 팩토리얼 0의 갯수 문제와 거의 유사한 문제
# 조합의 경우 분모, 분자의 2와 5의 갯수를 각각 헤아려 분자의 2, 5의 갯수에서 분모의 2, 5의 갯수를 각각 뺀 뒤
# 2와 5의 갯수중 작은 값을 취하면 된다. 팩토리얼의 경우와는 달리 결과로 나오는 2의 갯수가 5의 갯수보다 적을 수 있어
# 둘 다 헤아릴 필요가 있다.
# 분모는 n * n-1 * ... n-m+1,  분자는 1 * 2 * ... * m
def sol2004():
    n, m = map(int, input().split())
    ncount = [0, 0]
    mcount = [0, 0]
    s = n - m

    # 2의 갯수 카운트
    i = 2
    while(i <= n):
        # 1부터 n 까지의 모든 숫자를 소인수분해 했을 때 2의 갯수를 분모의 2의 갯수에 더함   (1 * 2 * ... * n)
        ncount[0] += n // i

        # 1부터 n-m 까지의 모든 숫자를 소인수분해 했을 때 2의 갯수를 분모의 2의 갯수에서 뺌 (1 * 2 * ... * n-m)
        if(i <= s):
            ncount[0] -= s // i

        # 1부터 m 까지의 모든 숫자를 소인수분해 했을 때 2의 갯수를 분자의 2의 갯수에 더함 (1 * 2 * ... * m)
        if(i <= m):
            mcount[0] += m // i
        i *= 2

    # 위 작업을 소인수를 5로 하여 수행
    i = 5
    while (i <= n):
        ncount[1] += n // i
        if (i <= s):
            ncount[1] -= s // i
        if (i <= m):
            mcount[1] += m // i
        i *= 5

    # 분모의 2와 5의 갯수에서 분자의 2와 5의 갯수를 각각 뺀 뒤 작은 쪽을 출력
    print(min(ncount[0]-mcount[0], ncount[1]-mcount[1]))
