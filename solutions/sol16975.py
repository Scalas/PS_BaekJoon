import sys
from math import ceil, log2

input = sys.stdin.readline


# 16975 수열과 쿼리 21
# 주어진 수열 A1~An 에 대해 m개의 쿼리를 처리하는 문제
# 1 i j k : Ai ~ Aj 에 k를 더하는 쿼리
# 2 x : Ax 를 출력하는 쿼리


# 세그먼트 트리를 구성하여 범위에 대한 덧셈을 부모노드에 저장하고
# 쿼리시에 부모노드의 값을 더하며 올라오는 방식으로 해결
def sol16975():
    n = int(input())
    seq = list(map(int, input().split()))
    cap = 2 ** ceil(log2(n))
    t = init_tree(seq, n, cap)
    answer = []
    # 쿼리 처리
    for _ in range(int(input())):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            update(t, cap, cmd[1]-1, cmd[2]-1, cmd[3])
        else:
            answer.append(query(t, cap, cmd[1]-1))
    return '\n'.join(map(str, answer))


# 세그먼트 트리 초기화
def init_tree(seq, n, cap):
    tree = [0] * (2 * cap)
    tree[cap:cap+n] = seq
    return tree


# update 함수
def update(tree, cap, l, r, v):
    l += cap
    r += cap
    while l < r:
        # l이 우측 자식노드라면 부모노드는 범위에 포함되지 않는다.
        # tree[l] 에 v를 합산하고 l += 1
        if l % 2:
            tree[l] += v
            l += 1

        # r이 좌측 자식노드라면 부모노드는 범위에 포함되지 않는다.
        # tree[r] 에 v를 합산하고 r += 1
        if not r % 2:
            tree[r] += v
            r -= 1
        l //= 2
        r //= 2
    # l == r일 경우 마지막 남은 l 혹은 r 번째 노드에 v를 합산
    if l == r:
        tree[l] += v


# 해당 인덱스의 수로부터 부모노드의 값을 더하며 타고올라간다
# 루트노드에 도달하면 더한 값을 반환
def query(tree, cap, x):
    x += cap
    res = 0
    while x:
        res += tree[x]
        x //= 2
    return res
