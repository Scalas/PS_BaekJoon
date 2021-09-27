import sys

input = sys.stdin.readline


# 9095 1, 2, 3 더하기
# 1, 2, 3을 더하여 숫자 n을 만드는 경우의 수를 구하는 문제
# 숫자 한개를 더하여 n이 되는 경우는 (n-3) + 3 , (n-2) + 2, (n-1) + 1 의 세 가지이다.
# 그러므로 dp[n] 이 1, 2, 3을 더하여 n을 만드는 경우의 수라고 할 때, dp[n] = dp[n-1] + dp[n-2] + dp[n-3] 이 된다.
def sol9095():
    # 숫자 n은 1부터 10까지의 정수
    dp = [0] * 11

    # 숫자 1, 2, 3을 만드는 경우의 수를 미리 구해둔다.
    dp[1:4] = [1, 2, 4]

    # dp[n] = dp[n-1] + dp[n-2] + dp[n-3] 임을 이용하여 동적계획법으로 모든 dp 값을 구한다.
    for i in range(4, 11):
        dp[i] = sum(dp[i - 3:i])

    # 테스트케이스들에 대한 답을 리스트화
    answer = [dp[i] for i in [*map(int, input().split())][1:]]

    # 출력형식에 맞춰 정답리스트 반환
    return '\n'.join(map(str, answer))
