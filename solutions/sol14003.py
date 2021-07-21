import sys
from bisect import bisect_left


# 14003 가장 긴 증가하는 부분 수열 5
# LIS 를 구하는 문제
# O(N^2)으로는 해결 불가능하며 O(NlogN) 알고리즘으로 풀어야함
# 14002 번 솔루션의 두 번째 방법을 참조
def sol14003(n, seq):
    lis, path = [], []
    for i in range(n):
        num = seq[i]
        if not lis or num > lis[-1]:
            lis.append(num)
            path.append(len(lis) - 1)
        else:
            p = bisect_left(lis, num)
            lis[p] = num
            path.append(p)

    l = len(lis) - 1
    res = []
    for p, num in list(zip(path, seq))[::-1]:
        if p == l:
            res.append(str(num) + ' ')
            l -= 1
    res.append(str(len(lis)) + '\n')
    return ''.join(res[::-1])
