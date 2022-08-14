import sys

input = sys.stdin.readline


# 6988 타일 밟기
# n개의 타일의 값이 오름차순으로 주어지고 값이 등차수열을 이루는 타일만을 연속으로 밟을 수 있을 때
# 3번 이상 연속으로 타일을 밟을 수 있는 경우의 밟은 타일의 값의 합 중 최댓값을 구하는 문제
def sol6988():
    n = int(input())
    tiles = list(map(int, input().split()))

    # dp[i][j] 는 차를 j로 유지하며 i번 타일까지 밟았을때 연속으로 밟은 타일의 수 - 1
    dp = [dict() for _ in range(n)]
    answer = 0
    for i in range(n):
        tile = tiles[i]
        for j in range(i):
            pre_tile = tiles[j]
            diff = tile - pre_tile
            dp[i][diff] = dp[j].get(diff, 0) + 1
            # 연속으로 밟은 타일의 수가 3 이상일 경우 지금까지 밟은 타일의 값의 합으로 answer 갱신
            if dp[i][diff] >= 2:
                answer = max(answer, calc(tile, diff, dp[i][diff] + 1))

    return answer


def calc(start, diff, cnt):
    return (start * cnt) - (cnt * (cnt - 1) // 2 * diff)
