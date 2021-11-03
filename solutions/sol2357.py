import sys
from math import ceil, log2

input = sys.stdin.readline
INF = 10 ** 9


# 2357 최솟값과 최댓값
# 세그먼트 트리를 사용하여 주어진 수열에서 구간별 최소, 최댓값을 찾는 문제
def sol2357():
    n, m = map(int, input().split())
    seq = [int(input()) for _ in range(n)]
    cap = 2 ** ceil(log2(n))
    t = init_tree(seq, n, cap)
    answer = []
    for _ in range(m):
        u, v = map(int, input().split())
        answer.append(' '.join(map(str, query(t, cap, u-1, v-1))))
    return '\n'.join(answer)


def init_tree(seq, n, cap):
    tree = [[INF, 0] for _ in range(2 * (cap + 1))]
    tree[cap:cap+n] = [[seq[i], seq[i]] for i in range(n)]
    for i in range(cap-1, 0, -1):
        lmin, lmax = tree[i*2]
        rmin, rmax = tree[i*2+1]
        tree[i] = [min(lmin, rmin), max(lmax, rmax)]
    return tree


def query(tree, cap, l, r):
    l += cap
    r += cap
    minv, maxv = INF, 0
    while l < r:
        if l % 2:
            minv = min(minv, tree[l][0])
            maxv = max(maxv, tree[l][1])
            l += 1
        if not r % 2:
            minv = min(minv, tree[r][0])
            maxv = max(maxv, tree[r][1])
            r -= 1
        l //= 2
        r //= 2
    if l == r:
        minv = min(minv, tree[l][0])
        maxv = max(maxv, tree[l][1])

    return [minv, maxv]