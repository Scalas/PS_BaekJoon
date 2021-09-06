import sys

input = sys.stdin.readline


# 1086 박성원
# 서로 다른 정수로 이루어진 집합이 주어졌을 때, 집합의 순열을 이어붙여 만든 정수가 k로 나누어 떨어질 확률을 구하는 문제
# 비트마스크 동적계획법 문제 중 하나이다.
def sol1086():
    # 집합의 크기(수의 갯수)
    n = int(input())

    # 집합 s
    s = [int(input()) for _ in range(n)]

    # 만들어진 수를 나눌 수 k
    k = int(input())

    # m[i][j] 는 j 와 i번째 수를 이어붙인 숫자를 k로 나눈 나머지
    m = [[((j * (10 ** len(str(s[i])))) % k + s[i] % k) % k for j in range(k)] for i in range(n)]

    # dp[i][j] 는 수의 선택상태가 i와 같을 때 순열로 만들어지는 수를 k로 나눈 나머지가 j인 경우의 수
    dp = [[0] * k for _ in range(1 << n)]

    # 아무것도 고르지 않았을 때 나머지가 0인 경우의 수를 1로 초기화
    dp[0][0] = 1

    # 상태전이 시작
    for i in range((1 << n) - 1):
        for j in range(k):
            # 현재 상태에서 나머지가 j인 경우의 수가 0이라면 이로부터 파생되는 경우의 수도 0
            # 더이상 진행할 필요가 없음
            if dp[i][j] == 0:
                continue

            # 아직 고르지 않은 수에 대해
            for b in range(n):
                check = 1 << b
                if not (i & check):
                    # 나머지 j와 이 수를 합친 수를 k로 나눈 나머지는 m[b][j]
                    # 현재 상태의 경우의수가 그대로 dp[i | check][m[b][j]]로 전이되기 때문에
                    # 현자 상태의 경우의 수를 더해줌
                    dp[i | check][m[b][j]] += dp[i][j]

    # dp[(1<<n)-1] 까지 전이가 종료되고나면
    # 주어진 집합 전체의 순열로 이루어진 수를 k로 나눈 나머지가
    # 각각 0 ~ k-1 인 경우의 수를 모두 얻을 수 있다.
    # 그 경우의 수를 모두 더한것이 전체 경우의 수 (w)
    # 그 중 나머지가 0인 것이 k로 나누어 떨어지는 경우의 수 (v)
    v = dp[-1][0]
    w = sum(dp[-1])

    # 구하려는 것은 v / w 를 기약분수 형태로 나타낸 문자열
    # 기약분수로 나타내기 위해서는 v와 w의 최대공약수르 둘을 나누어준 뒤 출력형식에 맞춰 반환한다.
    g = gcd(v, w)
    return f'{v // g}/{w // g}'


# 유클리드 호제법에 따라 최대공약수를 구하는 함수
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a
