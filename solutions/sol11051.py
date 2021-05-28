import sys

input = sys.stdin.readline


# 11051 이항계수2
# 이항계수 c(n, k)를 구하는 문제

# 풀이 1. 단순히 정의대로 팩토리얼을 사용하여 푸는 방식
# 다른 언어에서는 입력값이 조금만 커져도 오버플로우가 발생하기 쉽상이지만
# 파이썬에서는 문제가 되지 않는다.
def sol11051():
    n, k = map(int, input().split())
    h, l = 1, 1
    for i in range(k):
        h *= n - i
        l *= k - i
    print((h // l) % 10007)


# 풀이 2. 동적계획법을 활용한 방식
# c(n, k) = c(n-1, k-1) + c(n-1, k) 임을 이용한 풀이
# 다른 언어로 포팅하여도 오버플로우가 발생할 위험이 없다
def sol11051():
    n, k = map(int, input().split())
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = 1
        dp[i][i] = 1
    for i in range(2, n+1):
        for j in range(1, k+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007
    print(dp[n][k])


# 풀이 3. 완전탐색을 활용하여 구하는 방식
# 탐색의 종료 조건을 k개를 뽑았을때로 할 경우 동적계획법과 같은 성능을 보인다
# 탐색의 종료 조건을 n개의 선택여부를 모두 정했을때로 할 경우 재귀의 깊이가 증가하여 더 느려진다
# 대신 반환문의 조건을 조금 손보는 것으로 k가 범위의 형태로 주어질 때도 사용 가능하다
def sol11051_3():
    n, k = map(int, input().split())
    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    def dfs(i, c):
        if (i == n):
            return 1 if c == k else 0

        if dp[i + 1][c] == -1:
            dp[i + 1][c] = dfs(i + 1, c)
        if dp[i + 1][c + 1] == -1:
            dp[i + 1][c + 1] = dfs(i + 1, c + 1)

        return (dp[i + 1][c] + dp[i + 1][c + 1]) % 10007

    print(dfs(0, 0))


