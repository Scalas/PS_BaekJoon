import sys

input = sys.stdin.readline


# 1256 사전
# n개의 a와 m개의 z로 이루어진 문장을 담은 사전에서
# 사전순으로 k번째 문장을 찾는 문제
def sol1256():
    n, m, k = map(int, input().split())

    # 초기 a와 z의 갯수
    a, z = n, m

    # n이 m보다 작도록 한다
    if n > m:
        n, m = m, n

    # dp[n][m]은 문자 두개가 각각 n개, m개일때 만들 수 있는 모든 문자열의 갯수
    # dp[n][m] = dp[m][n]이므로 dp[n][0~n-1] 은 구할 필요가 없다
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(m+1):
        dp[0][i] = 1
    for i in range(1, n+1):
        dp[i][i] = dp[i-1][i] * 2
        for j in range(i+1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # 만들수있는 문자열의 갯수보다 k가 클 경우 -1 반환
    if dp[-1][-1] < k:
        return -1

    answer = []
    while a and z:
        # 이번 문자로 a를 선택할 경우 만들 수 있는 문자열의 수
        if a-1 < z:
            ac = dp[a-1][z]
        else:
            ac = dp[z][a-1]

        # ac가 k 이상일 경우 k번째 문자열을 구하려면 이번 문자는 a여야 함
        if k <= ac:
            answer.append('a')
            a -= 1
        # ac가 k보다 작을 경우 k번째 문자열을 구하려면 이번 문자는 z여야 함
        else:
            answer.append('z')
            z -= 1
            k -= ac
    # 어느 한쪽 문자의 갯수를 모두 사용했을 경우 갯수가 남아있는 문자를 남은 갯수만큼 이어붙임
    if not a:
        answer.append('z'*z)
    else:
        answer.append('a'*a)
    return ''.join(answer)
