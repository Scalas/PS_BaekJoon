import sys

input = sys.stdin.read


# 5582 공통 부분 문자열
# LCS 의 또다른 형태인 최장 공통 부분 문자열을 구하는 문제
# 최장 공통 부분 수열과 달리 원소가 연속해야 하기 때문에 동적계획법에 사용되는 점화식이 조금 달라진다.
# 파이썬 기준으론 시간, 메모리조건이 상당히 빡빡했기 때문에 dp 리스트의 사이즈를 N * M이 아니라 N * 2로 하여
# 재활용하는 형태로 간신히 통과하였다.
def sol5582():
    a, b = map(list, input().split())
    n, m = len(a)+1, len(b)+1
    dp = [0] * m
    answer = 0
    for i in range(1, n):
        tdp = [0] * m
        for j in range(1, m):
            if a[i - 1] == b[j - 1]:
                tdp[j] = dp[j - 1] + 1
                if tdp[j] > answer:
                    answer = tdp[j]
        dp = tdp
    return answer
