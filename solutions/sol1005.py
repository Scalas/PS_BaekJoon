import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


# 1005 ACM 크래프트
# 건설 규칙과 건물을 완성하는데 걸리는 시간이 주어졌을 때,
# 특정 건물을 건설하는데 걸리는 최소시간을 구하는 문제.
# 위상 정렬에 동적계획법을 적용하여 해결할 수 있는 문제이다.
def sol1005():
    # dfs(d) = dp[d] 는 d 번 건물을 건설하기 위해 필요한 최소 비용
    def dfs(d):
        # 아직 건물 d를 건설하기 위한 최소비용이 계산되지 않았다면 계산에 들어간다.
        # 건물 d를 건설하기 위한 최소비용은 반드시 먼저 건설되어야할 건물의 최소 비용 중
        # 가장 큰 비용에 건물 d를 건설하기 위해 필요한 비용을 합친 값이 된다.
        if dp[d] == -1:
            dp[d] = max([dfs(p) for p in g[d]], default=0) + cost[d]

        # 건물 d를 건설하기 위한 최소 비용을 반환
        return dp[d]

    # 케이스별 정답 리스트
    answer = []
    for t in range(int(input())):
        # 건물 수 n, 건설 규칙 수 k
        n, k = map(int, input().split())

        # 각 건물을 완성하는데 필요한 시간
        cost = [0, *map(int, input().split())]

        # 그래프를 생성
        g = [[] for _ in range(n + 1)]
        for _ in range(k):
            x, y = map(int, input().split())

            # 이 문제의 경우 정확하게 건물 w를 짓는데 드는 최소 비용만을 구하는 문제
            # 노드 전체를 위상정렬하는 문제와 다르게 건물 w를 짓기 위해 지어야 하는
            # 건물들의 최소 비용만을 탐색하는 것이 효율적이기 때문에
            # 역탐색을 위해 그래프의 인접리스트에 갈 수 있는 노드가 아닌
            # 현재 노드로 올 수 있는 노드를 저장한다.
            g[y].append(x)

        # dfs(w)를 구하여 정답 리스트에 저장
        dp = [-1] * (n + 1)
        w = int(input()
        answer.append(dfs(w))

        # 출력 형식에 맞춰 정답 리스트 반환
    return '\n'.join(map(str, answer))