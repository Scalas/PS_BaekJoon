import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline


# 2533 사회망 서비스(SNS)
# 얼리어답터가 아닌 노드는 인접한 모든 노드가 얼리어답터여야 할 때
# 가능한 얼리어답터 수의 최솟값을 구하는 문제
# 최대 독립 집합의 크기를 구하는 문제의 정반대가 되는 문제이다


# 풀이 1 - 단순히 최대 독립 집합의 크기를 구한 뒤 전체 노드 수에서 감산
def sol2533_1():
    # 노드의 갯수
    n = int(input())

    # 트리 구성
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    # 탐색 함수
    def dfs(pre, cur):
        # 현재 노드가 최대 독립 집합에 포함되지 않을 때, 포함 될 때의 최대 독립 집합의 크기
        res = [0, 1]

        # 현재 노드의 자식 노드에 대해
        for nxt in g[cur]:
            if nxt != pre:
                inc, ninc = dfs(cur, nxt)
                # 현재 노드가 최대 독립 집합에 포함되지 않는다면
                # 자식 노드는 최대 독립 집합에 포함될 수도, 포함되지 않을 수도 있다.
                res[0] += max(inc, ninc)

                # 현재 노드가 최대 독립 집합에 포함된다면
                # 자식 노드는 최대 독립 집합에 포함될 수 없다.
                res[1] += inc
        return res

    # 전체 노드 수에서 최대 독립 집합의 크기를 뺀 값 반환
    return n - max(dfs(0, 1))


# 풀이 2 - dfs의 동작을 역으로 변경
def sol2533_2():
    # 노드의 갯수
    n = int(input())

    # 트리 구성
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    # 탐색 함수
    def dfs(pre, cur):
        # 현재 노드가 얼리어답터가 아닐 때, 얼리어답터일 때의 최소 얼리어답터 수
        res = [0, 1]

        # 현재 노드의 자식 노드에 대해
        for nxt in g[cur]:
            if nxt != pre:
                inc, ninc = dfs(cur, nxt)
                # 현재 노드가 얼리어답터가 아니라면 자식노드는 반드시 얼리어답터여야 한다
                res[0] += ninc

                # 현재 노드가 얼리어답터라면 자식노드는 얼리어답터일 수도, 아닐 수도 있다.
                res[1] += min(inc, ninc)
        return res

    # 최소 얼리어답터 수 반환
    return min(dfs(0, 1))
