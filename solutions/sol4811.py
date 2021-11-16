import sys

input = sys.stdin.readline


# 4811 알약
# n개의 알약이 든 병에서 약을 꺼내 반쪽짜리라면 그냥 먹고 W를,
# 한개짜리라면 반쪽을 먹은 뒤 나머지 반쪽을 다시 집어넣고 H를 출력할 때
# 나올 수 있는 모든 문자열의 갯수를 구하는 문제
def sol4811():
    answer = []

    # dp[i][j] 는 1개짜리 알약이 i개, 반개짜리 알약이 j개일 때 나올 수 있는 문자열의 갯수
    dp = [[0] * 61 for _ in range(31)]
    dp[0][0] = 1

    def dfs(w, h):
        if not dp[w][h]:
            cnt = 0
            # 한개짜리 알약을 먹는 경우
            # 한개짜리 알약의 갯수가 줄어들고 반개짜리 알약의 갯수가 늘어난다
            if w:
                cnt += dfs(w-1, h+1)

            # 반개짜리 알약을 먹는 경우
            # 반개짜리 알약의 갯수가 줄어든다
            if h:
                cnt += dfs(w, h-1)
            dp[w][h] = cnt
        return dp[w][h]

    while True:
        n = int(input())
        if not n:
            break
        answer.append(dfs(n, 0))

    return '\n'.join(map(str, answer))
