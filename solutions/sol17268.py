import sys

input = sys.stdin.readline
MOD = 987654321


# 17268 미팅의 저주
# n명의 사람이 원탁에 둘러앉고 두 사람씩 쌍을 맺을 때
# 연결관계가 교차하지 않도록 하는 경우의 수를 987654321로 나눈 나머지를 구하는 문제
# 단, n은 1만 이하의 짝수이다
def sol17268():
    n = int(input())
    dp = [1, 1]
    for i in range(4, n + 1, 2):
        res = 0
        # g칸 떨어진 상대와 쌍을 맺고 그 연결선을 기준으로 좌우로 갈라진 사람들끼리
        # 쌍을 맺는 경우의 수를 곱한 값을 모두 더해준다
        for g in range(0, i, 2):
            res = (res + dp[g // 2] * dp[(i - 2 - g) // 2]) % MOD
        dp.append(res)

    return dp[n // 2]
