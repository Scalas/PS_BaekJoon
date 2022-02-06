import sys

input = sys.stdin.readline


# 2157 여행
# n개의 도시 사이의 일방통행 항공편과 그 항공편의 기내식 점수가 주어지고
# 1번 도시부터 n번 도시까지 번호가 작은 도시에서 큰 도시로만 이동 가능하고
# 지날 수 있는 최대 도시 수가 m개일 때(1번 n번 포함) 먹을 수 있는 기내식의
# 점수의 합의 최댓값을 구하는 문제
def sol2157():
    n, m, k = map(int, input().split())
    # 같은 경로라면 보다 기내식 점수가 높은 항공편만 저장
    # 번호가 큰 도시에서 작은 도시로의 항공편은 무시
    g = [[0] * n for _ in range(n)]
    for _ in range(k):
        u, v, w = map(int, input().split())
        if u < v:
            g[u-1][v-1] = max(g[u-1][v-1], w)

    # dp[i] 는 i번 도시에 도달하기까지 먹을 수 있는 기내식의 점수의 합의 최댓값
    dp = [g[0][i] for i in range(n)]

    # m회 이하의 도시를 거쳐 얻을 수 있는 기내식 점수합의 최댓값
    answer = dp[-1]

    # 지나간 도시의 갯수
    # 1번도시에서 출발하기에 초기값은 1
    cnt = 1

    # m개의 도시를 지날 때 까지 반복
    while cnt < m:
        ndp = [0] * n
        cnt += 1
        # cnt-1개의 도시를 거쳐 cur 번째 도시에 도달
        for cur in range(n):
            # 도달할 수 없다면 continue
            if not dp[cur]:
                continue

            # cur 번째 도시에서 갈 수 있는 도시
            for nxt in range(cur+1, n):
                if not g[cur][nxt]:
                    continue
                # cnt개의 도시를 거쳐 nxt 번째 도시에 도달했을 때
                # 얻을 수 있는 기내식점수 총합의 최댓값을 갱신
                ndp[nxt] = max(ndp[nxt], dp[cur] + g[cur][nxt])

        # n번째 도시에 도달한 경우로 answer 를 갱신
        answer = max(answer, dp[-1])

        # dp값 갱신
        dp = ndp

    return answer
