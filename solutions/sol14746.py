import sys
from bisect import bisect_right
from collections import defaultdict

input = sys.stdin.readline
INF = float('inf')


# 14746 Closest Pair
# 두 평행선 위에 있는 점들의 x좌표가 주어졌을 때
# 각 평행선에서 하나씩 점을 골라 두 점의 거리를 쟀을 때
# 그 값이 최솟값이 되는 경우의 거리와
# 그 거리를 만족하는 두 점의 쌍의 갯수를 구하는 문제
def sol14746():
    n, m = map(int, input().split())
    u, v = map(int, input().split())
    seq_a = sorted(map(int, input().split()))
    seq_b = sorted(map(int, input().split()))

    closest = defaultdict(int)

    # 평행선 a 위의 모든 점에 대해
    # 평행선 b 위의 가장 가까운 두 점(양쪽으로)을 구하면
    # 그 거리중 최솟값이 최소 거리가 된다
    for num in seq_a:
        idx = bisect_right(seq_b, num)
        l_diff = abs(num - seq_b[idx - 1]) if idx > 0 else INF
        r_diff = abs(num - seq_b[idx]) if idx < m else INF
        min_diff = min(l_diff, r_diff)
        if l_diff == r_diff:
            closest[min_diff] += 2
        else:
            closest[min_diff] += 1
    min_diff = min(closest.keys())
    min_count = closest[min_diff]

    return f'{min_diff + abs(u - v)} {min_count}'
