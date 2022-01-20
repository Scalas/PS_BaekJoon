import sys
from bisect import bisect_left

input = sys.stdin.readline


# 11568 민균이의 계략
# 주어진 수열에서 최장 증가 수열의 길이를 구하는 문제
def sol11568():
    n = int(input())
    f, *seq = map(int, input().split())
    lis = [f]
    for num in seq:
        if num > lis[-1]:
            lis.append(num)
        else:
            lis[bisect_left(lis, num)] = num
    return len(lis)
