import sys

input = sys.stdin.readline


# 2606 바이러스
# 컴퓨터의 연결상태가 주어졌을 때 1번컴퓨터가 바이러스에 걸리면 감염되는 컴퓨터의 갯수를 구하는 문제
# DFS 혹은 BFS로 연결된 정점을 모두 탐색한 뒤 탐색한 정점의 수 - 1 을 하면 구할 수 있다
def sol2606():
    n = int(input())
    m = int(input())
    g = [[] for _ in range(n + 1)]
    for i in range(m):
        s, e = map(int, input().split())
        g[s].append(e)
        g[e].append(s)

    def dfs(node):
        for adj in g[node]:
            if not visit[adj]:
                visit[adj] = True
                dfs(adj)

    visit = [False] * (n + 1)
    visit[1] = True
    dfs(1)
    return visit.count(True) - 1


if __name__ == '__main__':
    print(sol2606())
