import sys

input = sys.stdin.readline


# 1613 역사
# 역사적 사건 n개와 그 전후관계 k개가 주어졌을 때
# 두 사건의 전후관계를 묻는 쿼리 s개에 대해 답을 구하는 문제
# 쿼리 u, v 에 대한 답은
# u가 v보다 먼저 일어났을 경우 -1, 나중에 일어났을 경우 1, 알 수 없을 경우 0
def sol1613():
    n, k = map(int, input().split())
    g = [list() for _ in range(n+1)]
    for _ in range(k):
        u, v = map(int, input().split())
        g[u].append(v)

    # path[i]는 사건 i 이후에 일어났음을 알 수 있는 사건의 리스트
    path = [set() for _ in range(n+1)]

    def dfs(cur):
        if not path[cur]:
            for nxt in g[cur]:
                path[cur].add(nxt)
                path[cur] |= dfs(nxt)
        return path[cur]

    # dfs로 사건의 전후관계 조사
    for i in range(1, n+1):
        if not path[i]:
            dfs(i)

    # 쿼리 처리
    answer = []
    for _ in range(int(input())):
        u, v = map(int, input().split())
        if v in path[u]:
            answer.append(-1)
        elif u in path[v]:
            answer.append(1)
        else:
            answer.append(0)

    return '\n'.join(map(str, answer))
