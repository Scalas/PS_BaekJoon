import sys

input = sys.stdin.readline


# 1695 팰린드롬 만들기
# 주어진 수열에 수를 더하여 팰린드롬이 되게 하려고 할 때
# 더해야할 수의 최소갯수를 구하는 문제
def sol1695():
    n = int(input())
    seq = list(map(int, input().split()))

    # 길이가 1인 수열은 팰린드롬이기 때문에 더할 필요 없음
    if n == 1:
        return 0

    # 길이가 2인 수열은 두 수가 같다면 이미 팰린드롬이기에 더할 필요가 없으며
    # 두 수가 서로 다르다면 1개를 더하여 팰린드롬으로 만들 수 있다.
    if n == 2:
        return 1 if seq[0] != seq[-1] else 0

    # dp[i][j] 는 seq[i:j+1]이 팰린드롬이 되기 위해 더해야할 숫자의 최소 갯수
    dp = [[0] * n for _ in range(n)]
    for i in range(n-1):
        if seq[i] != seq[i+1]:
            dp[i][i+1] = 1

    for g in range(2, n):
        for i in range(n-g):
            j = i + g
            # 양 끝의 숫자가 같다면 양 끝을 제외한 범위를 팰린드롬으로 만들기 위해 필요한 갯수
            if seq[i] == seq[j]:
                dp[i][j] = dp[i+1][j-1]
            # 양 끝의 숫자가 다르다면 왼쪽에 숫자를 더하거나 오른쪽의 숫자를 더한 경우중 최솟값
            else:
                dp[i][j] = min(dp[i][j-1] + 1, dp[i+1][j] + 1)

    # 수열의 처음부터 마지막까지의 부분을 팰린드롬으로 만들기 위해 더해야할 수의 최소 갯수
    return dp[0][-1]
