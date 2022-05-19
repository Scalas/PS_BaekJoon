import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10 ** 9


# 1486 등산
# 각 위치의 높이가 적혀있는 n * m 격자형태의 지도가 주어지고
# 낮은곳에서 높은곳으로의 이동은 높이차의 제곱만큼의 시간이, 
# 높은곳에서 낮은곳으로의 이동은 1만큼의 시간이 걸린다.
# 한번에 이동 가능한 최대 높이차가 t이고 d시간안에 다시 (0, 0)으로 돌아와야 할 때
# 도달할 수 있는 최대 높이를 구하는 문제
def sol1486():
    n, m, t, d = map(int, input().split())
    board = [list(map(atoi, input().rstrip())) for _ in range(n)]

    # 그래프 형태로 변환
    g = [[] for _ in range(n * m)]
    idx = 0
    for i in range(n):
        for j in range(m):
            # 위쪽 인접칸
            if i > 0:
                ni, nj = i - 1, j
                diff = board[i][j] - board[ni][nj]
                # 높이차가 t 이하일 때만 갈 수 있음
                if abs(diff) <= t:
                    # 현재 위치보다 낮거나 같은 곳일 경우
                    if diff >= 0:
                        g[idx].append((idx - m, 1))

                    # 높은 곳일 경우
                    else:
                        g[idx].append((idx - m, diff**2))
            # 아래쪽 인접칸
            if i < n - 1:
                ni, nj = i + 1, j
                diff = board[i][j] - board[ni][nj]
                # 높이차가 t 이하일 때만 갈 수 있음
                if abs(diff) <= t:
                    # 현재 위치보다 낮거나 같은 곳일 경우
                    if diff >= 0:
                        g[idx].append((idx + m, 1))

                    # 높은 곳일 경우
                    else:
                        g[idx].append((idx + m, diff**2))

            # 왼쪽 인접칸
            if j > 0:
                ni, nj = i, j - 1
                diff = board[i][j] - board[ni][nj]
                # 높이차가 t 이하일 때만 갈 수 있음
                if abs(diff) <= t:
                    # 현재 위치보다 낮거나 같은 곳일 경우
                    if diff >= 0:
                        g[idx].append((idx - 1, 1))

                    # 높은 곳일 경우
                    else:
                        g[idx].append((idx - 1, diff**2))

            # 오른쪽 인접칸
            if j < m - 1:
                ni, nj = i, j + 1
                diff = board[i][j] - board[ni][nj]
                # 높이차가 t 이하일 때만 갈 수 있음
                if abs(diff) <= t:
                    # 현재 위치보다 낮거나 같은 곳일 경우
                    if diff >= 0:
                        g[idx].append((idx + 1, 1))

                    # 높은 곳일 경우
                    else:
                        g[idx].append((idx + 1, diff**2))
            idx += 1

    # (0, 0)으로부터 모든 칸으로의 최단거리
    dp = [INF] * (n * m)
    q = [(0, 0)]
    dp[0] = 0
    while q:
        dst, cur = heappop(q)
        if dst > dp[cur]:
            continue

        for nxt, dist in g[cur]:
            if dst + dist < dp[nxt]:
                dp[nxt] = dst + dist
                heappush(q, (dp[nxt], nxt))

    # 각 칸과의 왕복 최단거리가 d 이하인 칸의 높이중 최댓값을 구한다
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] <= answer:
                continue
            idx = i * m + j
            if dp[idx] >= d:
                continue
            idp = [INF] * (n * m)
            q = [(0, idx)]
            idp[idx] = 0
            while q:
                dst, cur = heappop(q)
                if dst > idp[cur]:
                    continue

                for nxt, dist in g[cur]:
                    if dst + dist < idp[nxt]:
                        idp[nxt] = dst + dist
                        heappush(q, (idp[nxt], nxt))
            if dp[idx] + idp[0] <= d:
                answer = max(answer, board[i][j])
    return answer


# 알파벳을 높이로 변환
def atoi(char):
    if char.isupper():
        return ord(char) - ord('A')
    else:
        return ord(char) - ord('a') + 26
