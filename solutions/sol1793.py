import sys

input = sys.stdin.read


# 1793 타일링
# 2 * n 직사각형을 2 * 1, 2 * 2 타일로 채울 수 있는 방법의 수를 구하는 문제
def sol1793():
    case = list(map(int, input().split()))
    n = max(case)
    dp = [1, 1]
    for _ in range(n-1):
        dp.append(dp[-1] + dp[-2] * 2)
    return '\n'.join(map(str, [dp[c] for c in case]))
