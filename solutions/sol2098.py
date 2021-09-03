import sys

input = sys.stdin.readline
INF = 10 ** 9


def sol2098():
    # 도시의 갯수
    n = int(input())

    # 각 도시로부터 다른 도시로 가는데 드는 비용
    # 0일 경우 갈 수 없음을 의미하기 때문에 비용을 INF로 함
    w = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if w[i][j] == 0: w[i][j] = INF

    # dp[i][visited] 는 현재 i번째 도시에 있고 도시의 방문상태가 visited 일 때
    # 남은 도시를 모두 방문한 뒤 처음 도시로 돌아가는데 드는 비용의 최솟값이 된다.
    dp = [[-1] * (1 << n) for _ in range(n)]

    # 모든 도시를 방문한 상태의 visited값
    complete = (1 << n) - 1

    # 완전탐색 함수
    def dfs(cur, visited):
        # 만약 모든 도시를 방문했다면
        # 현재 위치에서 처음 도시로 가는 데 드는 비용을 반환
        if visited == complete:
            return w[cur][0]

        # 아직 계산하지 않은 경우라면
        if dp[cur][visited] == -1:
            # 다음 도시로 가는거리 w[cur][i] 와 다음 단계dfs(i, visited|(1<<i))의 합 중
            # 가장 작은 값이 dp[cur][visited] 가 된다.
            res = INF
            for i in range(1, n):
                check = 1 << i
                if w[cur][i] and not (visited & check):
                    res = min(res, dfs(i, visited | check) + w[cur][i])
            dp[cur][visited] = res

        # 현재 cur 도시에 있고 방문 상태가 visited일 때
        # 모든 도시를 거쳐 처음 도시로 돌아가기 위한 최소비용을 반환
        return dp[cur][visited]

    # 어느 점을 시작점으로 잡더라도 외판원 문제의 정답은 같다
    # 만약 한 점에서 순회경로를 찾지 못한다면 방문할 수 없는 점이 존재한다는 의미이기 때문에
    # 그 그래프에서는 순회경로가 존재하지 않는다
    return dfs(0, 1)
