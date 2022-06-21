import sys

input = sys.stdin.readline


# 12851 숨바꼭질 2
# 직선좌표 0 ~ 10만 사이의 좌표값 n과 k가 주어지고
# n에서 시작하여 매 시간마다 -1, +1, *2 의 좌표로 이동할 수 있을 때
# k로 이동하는데 걸리는 최소시간과 최소시간으로 k로 갈 수 있는 경우의 수를 구하는 문제
def sol12851():
    n, k = map(int, input().split())

    # dp[i] 는 n에서 i로 최단시간에 가는 경우의 수
    # visited[i] 는 n에서 i에 도달하는데 걸린 최소시간
    dp = [0] * 200001
    visited = [-1] * 200001
    dp[n] = 1
    visited[n] = 0
    q = [n]
    time = 0
    while q:
        time += 1
        nq = []
        for cur in q:
            if cur == k:
                return '\n'.join(map(str, [time - 1, dp[k]]))

            # 왼쪽으로 걷기
            if cur > 0:
                nxt = cur - 1
                if visited[nxt] < 0:
                    visited[nxt] = time
                    dp[nxt] += dp[cur]
                    nq.append(nxt)
                elif visited[nxt] == time:
                    dp[nxt] += dp[cur]

            # 오른쪽으로 걷기
            if cur < k:
                nxt = cur + 1
                if visited[nxt] < 0:
                    visited[nxt] = time
                    dp[nxt] += dp[cur]
                    nq.append(nxt)
                elif visited[nxt] == time:
                    dp[nxt] += dp[cur]

            # 2 * x의 위치로 이동하기
            if cur < (2 * k / 3):
                nxt = cur * 2
                if visited[nxt] < 0:
                    visited[nxt] = time
                    dp[nxt] += dp[cur]
                    nq.append(nxt)
                elif visited[nxt] == time:
                    dp[nxt] += dp[cur]
        q = nq
