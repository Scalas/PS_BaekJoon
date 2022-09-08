import sys

input = sys.stdin.readline


# 7976 수열
# n개의 수로 이루어진 수열에서 연속한 k개의 수의 합이 모두 짝수가 되면 그 수열을 짝합수열이라고 한다.
# n과 k, n개의 수로 이루어진 수열이 주어지고 이중 몇 개의 수를 원하는 대로 변경 가능할 떄
# 수열을 짝합수열로 만들기 위해 바꿔야할 수의 최솟값을 구하는 문제
def sol7976():
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))

    # 연속한 k개의 수와 그 다음 수 (k + 1 번 째)를 확인
    # 홀수는 1, 짝수는 0으로 표현할 때, k + 1 개의 수의 패턴에는 규칙이 있다.
    # seq[1] ~ seq[k] 의 수의 합이 짝수고 seq[2] ~ seq[k + 1] 또한 짝수이려면
    # seq[1] 과 seq[k + 1] 모두 짝수이거나 모두 홀수여야 한다.
    # 즉, seq[i] % 2 = seq[i - k] % 2 가 성립한다.

    # count[i][j]는 길이 k인 패턴의 i번째 인덱스에 해당하는 숫자를 2로 나눈 나머지가 j인 갯수
    count = [[0] * 2 for _ in range(k)]

    # dp[i][j] 는 길이 k인 패턴의 i번째 인덱스까지의 합을 2로 나눈 나머지가 j이기 위해 바꿔야할 숫자의 최소 갯수
    dp = [[0] * 2 for _ in range(k)]

    # count 계산
    for i in range(n):
        count[i % k][seq[i] % 2] += 1
    
    # dp 계산 
    dp[0][0], dp[0][1] = count[0][1], count[0][0]
    for i in range(1, k):
        dp[i][0] = min(dp[i - 1][0] + count[i][1], dp[i - 1][1] + count[i][0])
        dp[i][1] = min(dp[i - 1][0] + count[i][0], dp[i - 1][1] + count[i][1])
        
    # 패턴 전체의 합이 짝수가 되기 위해 바꿔야할 숫자의 최소 갯수 반환
    return dp[k - 1][0]
