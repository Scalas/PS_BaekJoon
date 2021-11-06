import sys
from math import ceil, log2

input = sys.stdin.readline


# 12899 데이터 구조
# 1 ~ 2000000 사이의 자연수를 저장할 수 있는 데이터베이스에
# 자연수 x를 추가하거나 x 번째로 작은 수를 출력하고 제거하는 쿼리를 n개 처리하는 문제

# 저장할 수의 범위인 2000000을 기준으로 세그먼트 트리를 구성하여 데이터베이스에 들어있는
# 각 숫자의 갯수를 카운팅한 값을 저장한다. 각 노드가 데이터베이스에 들어있는 숫자 중 자신의
# 범위에 해당하는 숫자의 갯수를 저장하고있다고 생각하면 쉽다.
def sol12899():
    n = int(input())
    cap = 2 ** (ceil(log2(2000000)))
    tree = [0] * (2 * cap)
    answer = []
    # n개의 쿼리 처리
    for _ in range(n):
        t, x = map(int, input().split())
        if t == 1:
            update(tree, cap, x-1)
        else:
            answer.append(query(tree, cap, x))

    return '\n'.join(map(str, answer))


# update 함수
def update(tree, cap, idx):
    idx += cap
    # 숫자 삽입할 숫자에 해당하는 노드와 그 조상노드들의 값을 1씩 증가
    while idx:
        tree[idx] += 1
        idx //= 2


# query 함수
def query(tree, cap, idx):
    # 루트노드부터 리프노드까지 탐색시작
    pos = 1
    while pos < cap:
        # 해당 범위에서 숫자가 1개 제거될 예정이므로 갯수 1 감소
        tree[pos] -= 1
        left, right = pos*2, pos*2+1
        # 좌측 서브트리의 크기가 idx 이상이라면 좌측으로
        if tree[left] >= idx:
            pos = left
        # 작다면 idx 에서 좌측 서브트리의 크기만큼을 빼고 우측으로
        else:
            idx -= tree[left]
            pos = right
    # 도달한 리프노드의 인덱스 pos 가 삭제할 숫자에 해당하는 노드이며
    # pos + 1이 실제로 삭제된 숫자가 된다
    tree[pos] -= 1
    return pos - cap + 1
