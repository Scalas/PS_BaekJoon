import sys
from math import ceil, floor

input = sys.stdin.readline


# 1607 원숭이 타워
# 하노이의 탑의 기둥 4개짜리 버전
# Frame-Stewart conjecture 라는 특수한 알고리즘을 사용해야 시간내에 풀 수 있음
# 그다지 의미있는 문제는 아니지만 풀었으니 일단 올려둠
def sol1607():
    n = int(input())
    dp = [-1] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for num in range(2, n + 1):
        sq_min = floor((2 * num + 1)**.5)
        sq_max = ceil((2 * num + 1)**.5)

        dp[num] = min(2 * dp[num - sq_min + 1] + 2 ** (sq_min - 1) - 1, 2 * dp[num - sq_max + 1] + 2 ** (sq_max - 1) - 1)

    return dp[n] % 9901
