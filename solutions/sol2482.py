import sys

input = sys.stdin.read
mod = 1000000003


# 2482 색상환
# n개의 색이 있는 색상환에서 인접하지 않는 k개의 색을 고르는 경우의 수를 구하는 문제
# 동적계획법을 활용한 풀이와 조합을 활용한 풀이의 두 가지 접근법이 있다.

# 동적계획법을 활용한 풀이
def sol2482_1():
    # 색상의 갯수와 골라야할 색상의 수
    n, k = map(int, input().split())

    # dp[i][j] 는 i번까지의 색상리스트중 j개를 고르는 경우의 수
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # 0개를 고르는 경우는 항상 1이며 1개를 고르는 경우는 항상 색상의 갯수와 같다.
    for i in range(n + 1):
        dp[i][0] = 1
        dp[i][1] = i

    # 점화식에 따라 dp를 채워나간다
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j]) % mod

    # 양 끝이 인접할 경우를 고려하여 경우의 수를 구하여 반환한다
    return (dp[n - 3][k - 1] + dp[n - 1][k]) % mod


# 조합을 활용한 풀이
def sol2482_2():
    # 색상의 총 수 n, 골라야할 색상의 수 k
    n, k = map(int, input().split())

    # 골라야할 색상의 수가 총 색상 수의 절반을 넘기면 인접하지 않도록 고르는것은 불가능
    if k > n // 2:
        return 0

    # 1개의 색을 고르는 경우의 수는 총 색상 수와 같음
    if k == 1:
        return n

    # n-k개의 고르지 않은 수의 사이에 존재하는 슬롯 n-k+1 개에서 k개의 슬롯을 골라 수를 삽입
    # 양 끝 슬롯을 함께고르는 경우를 배제하기 위해 양 끝 슬롯을 제외한 n-k-1 개의 슬롯에서
    # k-2개의 슬롯을 고르는 경우의 수를 감산
    return (bc(n - k + 1, k) - bc(n - k - 1, k - 2)) % mod


# 이항계수를 반환하는 함수
def bc(a, b):
    b = min(b, a - b)
    u, v = 1, 1
    for i in range(b):
        u *= (a - i)
        v *= (1 + i)
    return u // v
