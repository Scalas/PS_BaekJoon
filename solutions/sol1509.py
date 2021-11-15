import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


# 1509 팰린드롬 분할
# 주어진 문자열을 분할하여 모든 부분이 팰린드롬이 되도록 할 때
# 분할된 문자열의 최소갯수를 구하는 문제
def sol1509():
    string = input().rstrip()
    length = len(string)

    # dp[i][j] 는 strign[i:j+1] 의 팰린드롬 분할 최소갯수
    dp = [[0] * length for _ in range(length)]

    # string[i:j+1] 이 팰린드롬이라면 dp[i][j] = 1
    for i in range(length):
        dp[i][i] = 1
        if i < length-1:
            dp[i][i+1] = 1 if string[i] == string[i+1] else 2

    for d in range(2, length):
        for i in range(length-d):
            j = i+d
            if string[i] == string[j] and dp[i+1][j-1] == 1:
                dp[i][j] = 1

    # 왼쪽부분이 팰린드롬을 이루도록(dp[l][mid] == 1)하는 mid값들에 대하여
    # 오른쪽 부분의 dp값(dp[mid+1][j]) 에 1을 더한 값 중 최댓값이 dp[i][j] 가 된다
    def palindrome_split(l, r):
        if not dp[l][r]:
            dp[l][r] = min([1 + palindrome_split(mid+1, r) for mid in range(l, r) if dp[l][mid]==1])
        return dp[l][r]

    return palindrome_split(0, length-1)

