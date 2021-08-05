import sys
from itertools import combinations

input = sys.stdin.read


# 1208 부분수열의 합 2
# 수열의 부분수열중 크기가 양수이고 합이 s가 되는 것의 갯수를 구하는 문제
# Meet in the middle 알고리즘을 활용하여 해결 가능하다.
def sol1208():
    n, s, *seq = map(int, input().split())
    mid = n // 2
    left, right = seq[:mid], seq[mid:]
    ls, rs = {}, {}
    for c in [map(sum, combinations(left, i)) for i in range(mid + 1)]:
        for t in c:
            ls[t] = ls.get(t, 0) + 1
    for c in [map(sum, combinations(right, i)) for i in range(n - mid + 1)]:
        for t in c:
            rs[t] = rs.get(t, 0) + 1

    res = 0
    for t in ls.keys():
        res += ls[t] * rs.get(s - t, 0)
    if s == 0:
        res -= 1
    return res
