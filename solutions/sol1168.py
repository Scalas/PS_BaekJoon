import sys
from math import ceil, log2
input = sys.stdin.readline


# 1168 요세푸스 문제 2
# 순환형태의 수열 1~n 에 대해 순차적으로 k번째 수를 지워나갈 때 숫자들을 지워진 순서대로 정렬하는 문제
# 12899 데이터구조 문제와 동일하게 수의 범위로 세그먼트 트리를 구성하여 k번쨰 숫자를 빠르게 찾는 방법을 사용하면 해결가능
def sol1168():
    n, k = map(int, input().split())
    cap = 2 ** ceil(log2(n))
    t = init_tree(n, cap)
    answer = []
    idx = k-1
    for _ in range(n-1):
        answer.append(query(t, cap, idx+1))
        n -= 1
        idx = (idx + k - 1) % n
    answer.append(query(t, cap, idx+1))
    return '<{}>'.format(', '.join(map(str, answer)))


def init_tree(n, cap):
    tree = [0] * (2 * cap)
    tree[cap:cap+n] = [1] * n
    for i in range(cap-1, 0, -1):
        tree[i] = tree[i*2] + tree[i*2+1]
    return tree


def query(tree, cap, idx):
    pos = 1
    while pos < cap:
        tree[pos] -= 1
        left, right = pos * 2, pos * 2 + 1
        if tree[left] >= idx:
            pos = left
        else:
            idx -= tree[left]
            pos = right
    tree[pos] -= 1
    return pos - cap + 1
