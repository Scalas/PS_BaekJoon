import sys
from math import log2, ceil

input = sys.stdin.readline
mod = 1000000007


# 11505 구간 곱 구하기
# 값의 변경이 발생하는 상황에서 구간의 곱을 구하는 문제
# 세그먼트 트리를 응용하여 해결 가능한 문제
def sol11505():
    n, m, k = map(int, input().split())
    seq = [int(input()) for _ in range(n)]
    cap = 2 ** ceil(log2(n))
    t = segtree_init(seq, n, cap)
    answer = []
    for _ in range(m+k):
        u, v, w = map(int, input().split())
        if u % 2:
            segtree_update(t, cap, v-1, w)
        else:
            answer.append(segtree_query(t, cap, v-1, w-1))
    return '\n'.join(map(str, answer))


def segtree_init(seq, n, cap):
    tree = [1] * (cap * 2 + 1)
    tree[cap:cap+n] = seq
    for i in range(cap-1, 0, -1):
        tree[i] = (tree[i*2] * tree[i*2+1]) % mod
    return tree


def segtree_update(tree, cap, idx, data):
    idx += cap
    tree[idx] = data
    idx //= 2
    while idx > 0:
        tree[idx] = (tree[idx * 2] * tree[idx * 2 + 1]) % mod
        idx //= 2


def segtree_query(tree, cap, l, r):
    l += cap
    r += cap
    res = 1
    while l < r:
        if l % 2:
            res = (res * tree[l]) % mod
            l += 1
        if not r % 2:
            res = (res * tree[r]) % mod
            r -= 1
        l //= 2
        r //= 2
    if l == r:
        res = (res * tree[l]) % mod
    return res




