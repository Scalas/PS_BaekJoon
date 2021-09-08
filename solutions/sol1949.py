import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline


# 1949 우수 마을
# 서로 인접하지 않은 마을의 집합 중 인구 수의 총합이 가장 큰 경우의 총 인구수를 구하는 문제
# 즉, 트리의 최대독립집합 문제이다.
def sol1949():
    # 노드의 갯수
    n = int(input())

    # 각 노드의 가중치
    w = [0] + list(map(int, input().split()))

    # 트리 구성
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    # 탐색함수
    def dfs(pre, cur):
        # 현재 노드가 우수마을에 포함될지 여부에 따른 우수마을 주민 수 합의 최댓값
        res = [0, w[cur]]

        # 현재 노드의 자식노드들에 대해
        for nxt in g[cur]:
            if nxt != pre:
                inc, ninc = dfs(cur, nxt)
                # 현재 노드가 우수마을이 아니라면 다음 노드는 우수마을이거나 우수마을이 아닐 수 있다.
                res[0] += max(inc, ninc)

                # 현재 노드가 우수마을이라면 다음 노드는 우수마을이 아니어야 한다.
                res[1] += inc
        return res

    # 우수 마을 주민 수 합의 최댓값 반환
    return max(dfs(0, 1))
