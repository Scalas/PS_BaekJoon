import sys

input = sys.stdin.readline


# 4803 트리
# 그래프가 주어졌을 때, 그래프 내에 트리가 몇개 존재하는지 구하는 문제
# 트리는 사이클이 없는 그래프이기 때문에 부모를 제외한 연결된 노드를 탐색해나가다가
# 방문한적이 있는 노드를 발견할 경우 사이클이 존재하기에 트리가 아님을 알 수 있다.
# 이 탐색을 방문한적 없는 정점들에 대해 순차적으로 실시하면 해결 가능하다.
# 물론 사이클이 있는 그래프에 속한 노드를 모드 배제해야하기에 사이클을 발견해도 탐색을 중단해서는 안된다.
def sol4803():
    def dfs(parent, node):
        nonlocal isTree
        visit[node] = True
        for child in g[node]:
            if child == parent:
                continue
            if not visit[child]:
                dfs(node, child)
            else:
                isTree = False

    answer = []
    case = 1
    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            break
        g = [[] for _ in range(n + 1)]
        for _ in range(m):
            s, e = map(int, input().split())
            g[s].append(e)
            g[e].append(s)

        visit = [False] * (n + 1)
        cnt = 0
        for node in range(1, n + 1):
            if not visit[node]:
                isTree = True
                dfs(0, node)
                if isTree:
                    cnt += 1
        if cnt == 0:
            answer.append(f'Case {case}: No trees.')
        elif cnt == 1:
            answer.append(f'Case {case}: There is one tree.')
        else:
            answer.append(f'Case {case}: A forest of {cnt} trees.')
        case += 1
    return '\n'.join(answer)
