import sys

input = sys.stdin.readline
MOD = 1000007


# 1513 경로 찾기
# n, m 크기의 격자공간에 c개의 오락실의 위치가 번호순서대로 주어지고
# 오락실을 들를 경우 반드시 방문한 오락실 순서가 오름차순이 되도록 방문해야하며
# 이동은 우측 또는 아래로만 가능하다고 할 때, (0, 0)에서 (n - 1, m - 1)로 가는 경로중
# 오락실 방문 횟수가 0 ~ c 회인 경우의 수를 각각 구하는 문제
def sol1513():
    n, m, c = map(int, input().split())
    gr = [[0] * m for _ in range(n)]
    for i in range(c):
        u, v = map(int, input().split())
        gr[u - 1][v - 1] = i + 1

    # dp[i][j][cnt][last] 는 (i, j)에 도착해있고
    # 현재 칸까지 포함하여 cnt개의 오락실에 들렀으며
    # 마지막으로 간 오락실의 번호가 last 인 경우의 수
    dp = [[[[0] * (c + 1) for _ in range(c + 1)] for _ in range(m)] for _ in range(n)]

    # 시작 위치에 오락실이 있을 경우
    if gr[0][0]:
        dp[0][0][1][gr[0][0]] = 1
    # 시작 위치에 오락실이 없을 경우
    else:
        dp[0][0][0][0] = 1

    # 각 좌표를 대각선으로 방문
    for diag in range(n + m - 1):
        for i in range(max(diag - m + 1, 0), min(diag + 1, n)):
            j = diag - i

            cur = dp[i][j]

            # 아랫칸, 오른쪽칸
            down, right = None, None
            if i < n - 1:
                down = dp[i + 1][j]
            if j < m - 1:
                right = dp[i][j + 1]

            for cnt in range(c + 1):
                for last in range(c + 1):
                    if not cur[cnt][last]:
                        continue

                    if down:
                        nxt = gr[i + 1][j]

                        # 아랫칸이 오락실이 아닐 경우
                        # cnt, last는 변하지 않고 그대로 더해짐
                        if not nxt:
                            down[cnt][last] = (down[cnt][last] + cur[cnt][last]) % MOD
                        # 아랫칸이 오락실이고 마지막으로 간 오락실 번호보다 큰 경우
                        elif nxt > last:
                            down[cnt + 1][nxt] = (down[cnt + 1][nxt] + cur[cnt][last]) % MOD
                    if right:
                        nxt = gr[i][j + 1]

                        # 오른쪽칸이 오락실이 아닐 경우
                        # cnt, last는 변하지 않고 그대로 더해짐
                        if not nxt:
                            right[cnt][last] = (right[cnt][last] + cur[cnt][last]) % MOD
                        # 아랫칸이 오락실이고 마지막으로 간 오락실 번호보다 큰 경우
                        elif nxt > last:
                            right[cnt + 1][nxt] = (right[cnt + 1][nxt] + cur[cnt][last]) % MOD

    # 마지막 칸의 상태
    ac = dp[-1][-1]

    # 마지막 칸에 도달한 경우의 수 중에서 오락실 방문 횟수가 0 ~ c 인 경우의 수를 각각 출력
    return ' '.join(map(str, [sum(ac[i]) % MOD for i in range(c + 1)]))
