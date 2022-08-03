import sys

input = sys.stdin.readline


# 4256 이진트리의 pre-order, in-order 순회 결과가 주어졌을 때
# post-order 순회결과를 구하는 문제
def sol4256():
    t = int(input())
    answers = []
    for _ in range(t):
        n = int(input())

        pre_order = list(map(int, input().split()))
        in_order = list(map(int, input().split()))

        # pre-order 리스트의 값을 노드 번호 대신 해당 노드의 in-order 리스트에서의 인덱스로 치환
        node_index = [-1] * (n + 1)
        for i in range(n):
            node_index[in_order[i]] = i
        pre_order = [node_index[num] for num in pre_order]

        # post-order 순회 리스트
        post_order = []

        # (0, n) 구간부터 탐색 시작
        dfs(pre_order, in_order, 0, 0, n - 1, post_order)

        answers.append(' '.join(map(str, post_order)))

    return '\n'.join(answers)


# post-order 순회를 위한 함수
def dfs(pre_order, in_order, root_index, left, right, post_order):
    # 루트 위치
    root = pre_order[root_index]

    # 좌측 서브트리가 있는 경우
    left_size = root - left
    if left_size:
        dfs(pre_order, in_order, root_index + 1, left, root - 1, post_order)

    # 우측 서브트리가 있는 경우
    right_size = right - root
    if right_size:
        dfs(pre_order, in_order, root_index + left_size + 1, root + 1, right, post_order)

    # 루트 노드 탐색
    post_order.append(in_order[root])
