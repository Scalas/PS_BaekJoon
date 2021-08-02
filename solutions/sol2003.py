import sys

input = sys.stdin.readline


# 2003 수들의 합 2
# 주어진 수열의 연속 부분수열중 합이 m이 되는 것의 갯수를 구하는 문제
# 투 포인터를 사용하여 간단하게 해결 가능하다
def sol2003():
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))
    s, t = 0, 0
    res = 0
    for e in range(n):
        t += seq[e]
        while t > m and s <= e:
            t -= seq[s]
            s += 1
        if s > e:
            continue
        if t == m:
            res += 1
    return res

