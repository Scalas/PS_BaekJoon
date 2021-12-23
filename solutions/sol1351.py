import sys

input = sys.stdin.readline


# 1351 무한 수열
# 주어진 n, p, q에 대해서 A[i] = A[i // p] + A[i // q] 이고 A[0] 이 1일 때
# A[n] 의 값을 구하는 문제
def sol1351():
    n, p, q = map(int, input().split())
    dp = {0: 1}

    # 점화식이 주어진 간단한 문제지만 dp를 n 크기의 리스트로 잡기엔 n이 매우 크기 때문에
    # 딕셔너리를 사용하여 메모이제이션을 해주는 것으로 메모리 초과를 해결
    def dfs(num):
        if num not in dp:
            dp[num] = dfs(num // p) + dfs(num // q)
        return dp[num]

    return dfs(n)
