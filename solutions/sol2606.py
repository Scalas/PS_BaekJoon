import sys

input = sys.stdin.read


# 2606 바이러스
# 컴퓨터의 연결상태가 주어졌을 때 1번컴퓨터가 바이러스에 걸리면 감염되는 컴퓨터의 갯수를 구하는 문제
# DFS 혹은 BFS로 연결된 정점을 모두 탐색한 뒤 탐색한 정점의 수 - 1 을 하면 구할 수 있다
def sol2606():
    n, m, *links = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for i in range(0, m * 2, 2):
        g[links[i]].append(links[i + 1])
        g[links[i + 1]].append(links[i])

    for edge in g:
        edge.sort()

    print(dfs(g, 1, [0] * (n + 1))-1)


def dfs(g, v, visit):
    visit[v] = 1
    res = 1
    for nv in g[v]:
        if visit[nv] == 0:
            res += dfs(g, nv, visit)
    return res
