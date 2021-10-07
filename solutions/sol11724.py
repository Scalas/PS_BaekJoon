import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


# 11724 연결 요소의 개수
# 무향 그래프가 주어졌을 때 서로 연결된 노드들의 집합을 연결요소라고 한다면
# 그래프내에 연결 요소의 갯수가 몇개인지 구하는 문제

# dfs 를 활용한 풀이
def sol11724():
    # 노드와 간선의 갯수
    n, m = map(int, input().split())

    # 그래프 구성
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    # dfs 함수
    def dfs(cur):
        for nxt in g[cur]:
            if not visit[nxt]:
                visit[nxt] = True
                dfs(nxt)

    # 방문여부 체크
    visit = [False] * (n + 1)

    # 한 노드를 방문할 때마다 연결된 모든 노드를 방문처리 하기 때문에
    # 이 반복문에서 dfs 를 호출한 횟수가 곧 연결요소의 갯수가 된다.
    answer = 0
    for i in range(1, n + 1):
        if not visit[i]:
            visit[i] = True
            dfs(i)
            answer += 1

    # 정답 반환
    return answer
