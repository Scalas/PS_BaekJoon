import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


# 2150 Strongly Connected Component
# 강한 연결요소를 찾는 문제

# SCC 알고리즘중 하나인 코사라주(Kosaraju)의 알고리즘을 사용
def sol2150():
    v, e = map(int, input().split())

    # 정방향 그래프와 역방향 그래프를 생성
    g = [[] for _ in range(v + 1)]
    rg = [[] for _ in range(v + 1)]
    for _ in range(e):
        x, y = map(int, input().split())
        g[x].append(y)
        rg[y].append(x)

    # 정방향 그래프를 기준으로 dfs 실행
    visited = [False] * (v + 1)
    st = []
    for i in range(1, v + 1):
        if not visited[i]:
            dfs(g, i, visited, st)

    # 강한 연결요소의 갯수
    cnt = 0

    answer = [[0]]
    visited = [False] * (v + 1)
    # 역방향 그래프에 대한 dfs 실행
    # 서로 다른 강한 연결요소간에 왕복가능한 경로는 존재할 수 없기 때문에
    # 그래프를 위상정렬한 상태에서 마지막 노드로부터 거슬러올라가며 역그래프를 탐색하면
    # 서로 다른 강한 연결 요소를 구분할 수 있다. 정방향 그래프에 대한 dfs 로 얻은 스택이
    # 그래프를 위상정렬한 결과이므로 스택의 top 에서부터 순차적으로 역그래프에 대한 dfs를 실행한다.
    for i in st[::-1]:
        if not visited[i]:
            scc = []
            rdfs(rg, i, visited, scc)
            scc.sort()
            scc.append(-1)
            answer.append(scc)
            cnt += 1
    answer.sort()
    answer[0][0] = cnt
    return '\n'.join([' '.join(map(str, a)) for a in answer])


# 정방향 그래프에 행하는 dfs
# 가장 마지막에 탐색한 노드가 먼저 스택에 삽입되도록 한다(위상정렬)
def dfs(g, v, visited, st):
    visited[v] = True
    for nxt in g[v]:
        if not visited[nxt]:
            dfs(g, nxt, visited, st)
    st.append(v)


# 역방향 그래프에서 행하는 dfs
# 탐색한 노드를 모두 리스트에 담는다
def rdfs(g, v, visited, st):
    visited[v] = True
    st.append(v)
    for nxt in g[v]:
        if not visited[nxt]:
            dfs(g, nxt, visited, st)
