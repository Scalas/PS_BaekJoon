import sys
from math import ceil, log2

input = sys.stdin.readline


# 9345 디지털 비디오 디스크(DVDs)
# 선반의 l부터 r까지의 구간에 순서에 상관없이 l번부터 r번까지의
# 비디오가 들어있는지 여부를 구하는 문제
# 최소 최대 세그먼트 트리로 해결 가능하다.
def sol9345():
    answer = []
    for _ in range(int(input())):
        n, k = map(int, input().split())
        cap = 2 ** ceil(log2(n))
        seq = list(range(n))
        t = init_tree(seq, cap, n)
        for _ in range(k):
            u, v, w = map(int, input().split())
            if u == 0:
                update(t, cap, v, w)
            else:
                answer.append('YES' if query(t, n, cap, v, w) else 'NO')
    return '\n'.join(map(str, answer))


def init_tree(seq, cap, n):
    tree = [[n+1, 0] for _ in range(2 * cap)]
    tree[cap:cap+n] = [[i, i] for i in seq]
    for i in range(cap-1, 0, -1):
        ltree, rtree = tree[i*2], tree[i*2+1]
        tree[i] = [min(ltree[0], rtree[0]), max(ltree[1], rtree[1])]
    return tree


def update(tree, cap, src, dst):
    src += cap
    dst += cap
    tree[src], tree[dst] = tree[dst], tree[src]
    src //= 2
    dst //= 2
    while src != dst:
        ltree, rtree = tree[src*2], tree[src*2+1]
        tree[src] = [min(ltree[0], rtree[0]), max(ltree[1], rtree[1])]

        ltree, rtree = tree[dst*2], tree[dst*2+1]
        tree[dst] = [min(ltree[0], rtree[0]), max(ltree[1], rtree[1])]

        src //= 2
        dst //= 2


def query(tree, n, cap, lidx, ridx):
    res = [n+1, 0]
    low, high = lidx, ridx
    lidx += cap
    ridx += cap
    while lidx < ridx:
        if lidx % 2:
            a, b = tree[lidx]
            res[0] = min(res[0], a)
            res[1] = max(res[1], b)
            lidx += 1
        if not (ridx % 2):
            a, b = tree[ridx]
            res[0] = min(res[0], a)
            res[1] = max(res[1], b)
            ridx -= 1
        lidx //= 2
        ridx //= 2
    if lidx == ridx:
        a, b = tree[lidx]
        res[0] = min(res[0], a)
        res[1] = max(res[1], b)
    return res[0] >= low and res[1] <= high


if __name__ == '__main__':
    print(sol9345())
