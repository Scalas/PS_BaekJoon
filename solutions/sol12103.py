import sys

input = sys.stdin.readline


# 12103 짝합 수열
# 7976 수열 문제의 확장
# dp의 역추적까지 수행해야하는 문제
def sol12103():
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))

    # 변경해야할 횟수를 구하기 위한 count와 dp에 더해 역추적을 위한 trace 추가
    count = [[0] * 2 for _ in range(k)]
    dp = [[0] * 2 for _ in range(k)]
    trace = [[-1] * 2 for _ in range(k)]

    for i in range(n):
        count[i % k][seq[i] % 2] += 1

    dp[0][0] = count[0][1]
    dp[0][1] = count[0][0]
    trace[0][0] = 0
    trace[0][1] = 1

    # i번째 인덱스에서 어느 패턴(짝/홀)을 선택했는지 trace에 기록
    for i in range(1, k):
        pre_even = dp[i - 1][0] + count[i][1]
        pre_odd = dp[i - 1][1] + count[i][0]
        if pre_even < pre_odd:
            dp[i][0] = pre_even
            trace[i][0] = 0
        else:
            dp[i][0] = pre_odd
            trace[i][0] = 1

        pre_even = dp[i - 1][0] + count[i][0]
        pre_odd = dp[i - 1][1] + count[i][1]
        if pre_even < pre_odd:
            dp[i][1] = pre_even
            trace[i][1] = 1
        else:
            dp[i][1] = pre_odd
            trace[i][1] = 0

    change_count = dp[-1][0]

    # trace를 통해 최소 횟수의 변경으로 만들 수 있는 짝합수열 패턴을 구한 뒤
    # 기존 수열과 대조하여 맞지 않는 수를 1씩 증가시킴
    pattern = []
    remain = 0
    for cur in range(k - 1, -1, -1):
        p = trace[cur][remain]
        pattern.append(p)
        remain = abs(p - remain)
    pattern = pattern[::-1]

    for i in range(n):
        if seq[i] % 2 != pattern[i % k]:
            seq[i] += 1

    return str(change_count) + '\n' + ' '.join(map(str, seq))
