import sys

input = sys.stdin.readline


# 14606 피자
# 하나의 탑으로 쌓여있는 n개의 피자판을 한개씩으로 나눠야하고
# 2개 이상인 탑을 골라 두 개의 탑으로 분리할 때 두 탑의 높이를 곱한 만큼 즐거움을 느낀다고 할 때
# 모든 탑을 분리했을 때 느낄 수 있는 최대 즐거움의 크기를 구하는 문제
def sol14606():
    n = int(input())
    dp = [0] * (n+1)
    for i in range(2, n+1):
        for j in range(1, n//2+1):
            dp[i] = max(dp[i], dp[j] + dp[i-j] + j * (i-j))
    return dp[-1]
