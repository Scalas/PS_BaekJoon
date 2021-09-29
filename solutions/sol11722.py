import sys
from bisect import bisect_left

input = sys.stdin.read


# 11722 가장 긴 감소하는 부분 수열
# lis 와 반대로 감소하는 부분 수열중 가장 긴 것의 길이를 구하는 문제
# 단순히 주어진 수열을 뒤집은 뒤 가장 긴 증가 수열을 구해주면 해결할 수 있다.
def sol11722():
    n, *seq = map(int, input().split())
    seq = seq[::-1]
    lis = [seq[0]]
    for num in seq[1:]:
        if num > lis[-1]:
            lis.append(num)
        else:
            lis[bisect_left(lis, num)] = num
    return len(lis)

