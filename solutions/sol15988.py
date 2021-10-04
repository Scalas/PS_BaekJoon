import sys

input = sys.stdin.read


# 15988 1, 2, 3 더하기 3
# 정수 n을 1, 2, 3의 합으로 나타내는 방법의 총 갯수를 1000000009 로 나눈 나머지를 구하는 문제
def sol15988():
    # 나머지 연산을 위한 mod
    mod = 1000000009

    # 테스트케이스 리스트
    _, *case = map(int, input().split())

    # 케이스중 가장 큰 수
    m = max(case)

    # dp[n] 은 정수 n을 1, 2, 3의 합으로 나타내는 방법의 총 갯수를 1000000009 로 나눈 나머지
    dp = [0] * (m + 1)

    # dp[0] ~ dp[3] 을 미리 구하여 초기화
    dp[0:4] = [1, 1, 2, 4]

    # dp[n] = (dp[n-1] + dp[n-2] + dp[n-3]) % mod
    #       = ((dp[n-2] + dp[n-3] + dp[n-4]) + dp[n-2] + dp[n-3]) % mod
    #       = (2 * (dp[n-2] + dp[n-3] + dp[n-4]) - dp[n-4]) % mod
    #       = (2 * dp[n-1] - dp[n-4]) % mod
    for i in range(4, m + 1):
        dp[i] = (dp[i - 1] * 2 - dp[i - 4]) % mod

    # 각 테스트 케이스에 해당하는 dp 값을 출력 형식에 맞춰 반환
    return '\n'.join(map(str, [dp[c] for c in case]))
