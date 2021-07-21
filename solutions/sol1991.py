import sys

input = sys.stdin.readline


# 1991 트리 순회
# 트리를 전위, 중위, 후위 순으로 순회한 결과를 출력하는 문제
# dfs로 간단하게 해결가능
def sol1991():
    n = int(input())
    g = {}
    for _ in range(n):
        p, lc, rc = input().split()
        g[p] = (lc, rc)

    preorder, inorder, postorder = [], [], []

    def dfs(v):
        preorder.append(v)
        lc, rc = g[v]
        if lc != '.':
            dfs(lc)
        inorder.append(v)
        if rc != '.':
            dfs(rc)
        postorder.append(v)

    dfs('A')
    return '\n'.join(map(''.join, [preorder, inorder, postorder]))
