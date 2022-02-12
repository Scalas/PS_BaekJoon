import sys

input = sys.stdin.readline
mod = 987654321


# 1670 정상 회담 2
# 원탁에 앉은 n명의 사람이 서로 손이 교차하지 않도록 악수를 하는 경우의 수를 구하는 문제
def sol1670():
    n = int(input()) // 2
    dp = [1, 1, 2]
    for i in range(3, n+1):
        res = 0
        # 처음 악수를 한 두 사람을 기준으로 나머지 n-2명을 두 그룹으로 나눌 수 있음
        # 두사람이 인접해있다면 0 / n-2
        # 2칸 떨어져있다면 2 / n-4
        # 그러므로 dp[i] = sum([dp[j] * dp[i-2-j] for j in range(0, i-1, 2)])
        # 절반만큼은 중복
        for j in range(i // 2):
            res = (res + dp[j] * dp[i-j-1] * 2) % mod
        # 같은 크기의 그룹 두개로 분리된 경우가 존재한다면 합산
        if i % 2:
            res = (res + dp[i // 2] ** 2) % mod
        dp.append(res)
    return dp[n]
