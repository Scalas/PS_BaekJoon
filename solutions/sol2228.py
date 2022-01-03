import sys

input = sys.stdin.readline
INF = 10 ** 9


# 2228 구간 나누기
# 수열의 길이 n과 구간의 갯수 m이 주어졌을 때
# 1. 구간은 1개 이상의 연속된 수로 이루어진다.
# 2. 서로 다른 구간끼리 겹치거나 인접하지 않는다.
# 3. 반드시 정확히 m개의 구간을 선택해야한다.
# 위 세 가지 조건을 만족하여 m개의 구간을 골랐을 때,
# 구간의 합을 모두 더한 값 중 최댓값을 구하는 문제
def sol2228():
    n, m = map(int, input().split())
    seq = [int(input()) for _ in range(n)]

    # 누적합 전처리
    for i in range(n-1):
        seq[i+1] += seq[i]
    seq.append(0)

    # 현재 사용 가능한 구간의 시작이 i이고 고른 구간의 갯수가 j일 때
    # 앞으로 얻을 수 있는 최대 총 구간합
    dp = [{} for _ in range(n)]

    # 구간 m개 정하기
    def dfs(cur, cnt):
        # m개의 구간을 모두 고른 경우 더이상 얻을 수 있는 구간합은 없음
        if cnt == m:
            return 0

        # m개의 구간을 고르지 못하고 배열이 끝난경우 성립하지 않는 선택
        if cur >= n:
            return -INF

        # 아직 계산되지 않은 경우라면
        if cnt not in dp[cur]:
            res = -INF

            # cur부터 n-1 까지중 구간의 끝을 선택
            for nxt in range(cur, n):
                # (seq[cur:nxt+1] 의 합) +
                # (구간의 시작이 nxt+2이고 고른 구간의 갯수가 cnt+1일 때 얻을 수 있는 최대 총 구간합)
                res = max(res, dfs(nxt+2, cnt+1) + seq[nxt] - seq[cur-1])

            # 현재 구간을 넘기는 경우
            res = max(res, dfs(cur+1, cnt))

            # dp에 계산 결과를 저장
            dp[cur][cnt] = res

        return dp[cur][cnt]

    return dfs(0, 0)
