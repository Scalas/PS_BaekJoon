import sys
from math import ceil, log2

input = sys.stdin.readline


# 2042 구간 합 구하기
# 세그먼트 트리를 활용하여 중간중간 값의 갱신이 이뤄지는 상태에서
# 구간합을 구하는 문제
def sol2042():
    n, m, k = map(int, input().split())
    data = [int(input()) for _ in range(n)]
    cap = 2 ** ceil(log2(n))
    t = build_segtree(n, cap, data)
    answer = []
    for _ in range(m+k):
        u, v, w = map(int, input().split())
        if u == 1:
            update(t, cap, v-1, w)
        else:
            answer.append(query(t, cap, v-1, w-1))
    return '\n'.join(map(str, answer))


def build_segtree(n, cap, data):
    segtree = [0] * (2 * cap)
    segtree[cap:cap+n] = data[:]
    for i in range(cap-1, 0, -1):
        segtree[i] = segtree[i*2] + segtree[i*2+1]
    return segtree


def update(segtree, cap, idx, data):
    idx += cap
    diff = data - segtree[idx]
    while idx > 0:
        segtree[idx] += diff
        idx //= 2


def query(segtree, cap, lidx, ridx):
    res = 0
    lidx += cap
    ridx += cap
    while lidx < ridx:
        if lidx % 2:
            res += segtree[lidx]
            lidx += 1
        if not (ridx % 2):
            res += segtree[ridx]
            ridx -= 1
        lidx //= 2
        ridx //= 2
    if lidx == ridx:
        res += segtree[lidx]
    return res
