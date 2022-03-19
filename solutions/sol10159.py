import sys

input = sys.stdin.readline


# 10159 저울
# 물건의 갯수 n과 i번 물건과 j번 물건의 무게비교 결과를 나타내는 i j 쌍 m개가 주어질 때(i j 는 i 가 j 보다 무겁다는 의미)
# 모든 물건에 대해 무게 비교가 불가능한 물건의 갯수를 구하는 문제
def sol10159():
    n = int(input())
    m = int(input())

    # g[i] 는 i보다 가벼운 물건의 리스트
    g = [[] for _ in range(n)]

    # rg[i] 는 i보다 무거운 물건의 리스트
    rg = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x)-1, input().split())
        g[u].append(v)
        rg[v].append(u)

    # bfs(i) 는 i와 무게비교가 불가능한 물건의 수
    def bfs(i):
        # 자신을 제외한 물건의 갯수
        cnt = n-1

        # 자신보다 가벼운 물건의 수만큼 cnt -= 1
        visited = [False] * n
        q = [i]
        visited[i] = True
        while q:
            nq = []
            for cur in q:
                for nxt in g[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        nq.append(nxt)
                        cnt -= 1
            q = nq

        # 자신보다 무거운 물건의 수만큼 cnt -= 1
        q = [i]
        while q:
            nq = []
            for cur in q:
                for nxt in rg[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        nq.append(nxt)
                        cnt -= 1
            q = nq

        # 무게 비교가 불가능한 물건의 수 반환
        return cnt

    return '\n'.join(map(str, [bfs(i) for i in range(n)]))
