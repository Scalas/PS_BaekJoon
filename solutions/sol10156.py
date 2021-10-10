import sys

input = sys.stdin.readline


# 10156 과자
# 소지금 m 원으로 k 원짜리 과자를 n 개 살 때 모자란 액수를 구하는 문제
def sol10156():
    k, n, m = map(int, input().split())
    return max(k * n - m, 0)
