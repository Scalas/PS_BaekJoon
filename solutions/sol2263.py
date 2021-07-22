import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline


# 2263 트리의 순회
# 트리의 inorder와 postorder가 주어졌을 때 preorder를 출력하는 문제
# postorder의 마지막 노드는 그 트리의 루트이며
# inorder의 루트노드를 기준으로 왼쪽은 좌측 서브트리, 오른쪽은 우측 서브트리임을 이용하면
# 간단히 해결 가능하다.
def sol2263():
    n = int(input())
    inorder = list(map(int, input().split()))
    inidx = [0] * (n + 1)
    for i in range(n):
        inidx[inorder[i]] = i
    postorder = list(map(int, input().split()))

    preorder = []
    def dfs(s, e, ps, pe):
        # 현재 노드를 preorder에 append
        root = postorder[pe]
        preorder.append(root)

        # 리프노드일 경우 종료
        if s == e:
            return

        # 루트의 inorder 에서의 인덱스를 찾아 좌 우 서브트리에 대해 재귀호출
        root_idx = inidx[root]
        pmid = ps + root_idx - s
        if root_idx - 1 >= s:
            dfs(s, root_idx - 1, ps, pmid - 1)
        if root_idx + 1 <= e:
            dfs(root_idx + 1, e, pmid, pe - 1)


    dfs(0, n - 1, 0, n - 1)

    return ' '.join(map(str, preorder))



