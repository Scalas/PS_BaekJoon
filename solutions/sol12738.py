import sys
from bisect import bisect_left

input = sys.stdin.read


# 12738 가장 긴 증가하는 부분 수열 3
# LIS 알고리즘 문제
# 수열의 크기가 100만까지 커지기 때문에 O(N^2) 알고리즘은 사용할 수 없다
# 이분탐색과 dp를 활용한 LIS 알고리즘을 사용하면 O(NlogN) 의 시간복잡도로 해결할 수 있다.
def sol12738():
    n, f, *seq = map(int, input().split())

    lis = [f]
    for num in seq:
        if num > lis[-1]:
            lis.append(num)
        else:
            lis[bisect_left(lis, num)] = num

    return len(lis)
