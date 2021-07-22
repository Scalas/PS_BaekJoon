import sys
from bisect import bisect_left

sys.setrecursionlimit(100000)
input = sys.stdin.read


# 5639 이진 검색 트리
# 이진 검색 트리의 pre order 가 주어졌을 때 post order를 구하는 문제
# pre order 의 맨 앞은 트리의 루트이며 이진 검색 트리이기 때문에
# 루트보다 큰 수 이전의 수들은 모드 좌측 서브트리에 속하며 나머지는 우측 서브트리에 속한다
# 루트보다 큰 수의 위치는 이진탐색으로 빠르게 구할 수 있다.
def sol5639():
    preorder = list(map(int, input().split()))

    postorder = []

    def dfs(s, e):
        root = preorder[s]
        if s != e:
            mid = bisect_left(preorder, root, lo=s+1, hi=e+1)
            if mid > s + 1:
                dfs(s + 1, mid - 1)
            if mid <= e:
                dfs(mid, e)
        postorder.append(root)

    dfs(0, len(preorder) - 1)
    return ' '.join(map(str, postorder))
