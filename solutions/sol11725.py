import sys


# 11725 트리의 부모 찾기
# 트리의 루트를 정해줬을 때 각 노드들의 부모를 구하는 문제
# dfs 혹은 bfs로 간단히 해결가능
def sol11725(n, links):
    parent = [0] * (n + 1)
    g = [[] for _ in range(n + 1)]
    for a, b in links:
        g[a].append(b)
        g[b].append(a)

    st = [1]
    visit = [False] * (n + 1)
    while st:
        node = st.pop()
        for c in g[node]:
            if not visit[c]:
                parent[c] = node
                st.append(c)
                visit[c] = True
    return '\n'.join(map(str, parent[2:]))
