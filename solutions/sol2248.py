import sys

input = sys.stdin.readline


# 2248 이진수 찾기
# n자리 2진수 중에서 m개 이하의 비트만이 1인 수만을 골라 오름차순 정렬했을 때
# 그중 k번째 수를 구하는 문제
# 단, 이진수는 0으로 시작할 수있음
def sol2248():
    n, m, k = map(int, input().split())

    # dp[i][j]는 이항계수 c(i, j) - i개의 비트중 j개의 1인 비트를 선택
    # 1이 될 수 있는 비트는 m개 이하이기 때문에 j는 m을 넘지않음
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
        if i <= m:
            dp[i][i] = 1

    for i in range(1, n+1):
        for j in range(1, min(i, m+1)):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    # n자리 이진수의 각 자릿수
    answer = [0] * n

    # 1이 될 수 있는 비트의 자리수를 탐색
    while k > 1:
        for i in range(1, n+1):
            # m개 이하의 비트만이 1인 수를 k개 이상 만들 수 있는 비트수 i를 탐색
            if sum(dp[i][:m+1]) >= k:
                # i번째 비트(answer[i-1])를 1로 설정
                answer[i-1] = 1

                # i-1비트까지의 수를 인덱스 k에서 빼주고
                # i-1번째 비트가 1인 수 중에서 k번째 수를 다시 탐색
                # i-1번째 비트가 1이 되었기 때문에 1이 될 수 있는 비트의 수는 1 감소
                k -= sum(dp[i-1][:m+1])
                m -= 1
                break

    # 이진수의 각 자릿수를 합쳐 이진수를 만들어 반환
    return ''.join(map(str, answer[::-1]))
