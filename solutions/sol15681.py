import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline


# 15681 트리와 쿼리
# 간선에 가중치와 방향성이 없는 트리가 주어졌을 때, 각 노드를 루트 노드로 하는 서브트리의 크기(포함된 노드의 갯수)를 구하는 문제
# 트리 동적 계획법 문제이다.
def sol15681():
    n, r, q = map(int, input().split())

    # 트리 구성
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    # 서브트리의 크기
    sub = [0] * (n + 1)

    # 탐색 함수
    def dfs(node):
        # 자기 자신을 포함하기 때문에 시작 크기는 1
        sub[node] = 1

        # 자식 노드를 루트로 하는 서브트리의 크기를 모두 더한다
        for c in g[node]:
            if not sub[c]:
                sub[node] += dfs(c)

        # 자신이 루트 노드인 서브트리의 크기 반환
        return sub[node]

    # 루트 노드로부터 탐색 시작
    dfs(r)

    # 각 쿼리에 대한 해답을 반환
    return '\n'.join([str(sub[int(input())]) for _ in range(q)])
