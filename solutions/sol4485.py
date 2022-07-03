import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10 ** 9


# 4485 녹색 옷 입은 애가 젤다지?
# n * n 격자공간에 각 칸에 도달할 때마다 잃게되는 금액이 주어졌을 때
# (0, 0)에서 (n - 1, n - 1) 에 도달하는 데 잃게되는 금액의 최솟값을 구하는 문제
def sol4485():
    answers = []
    while True:
        n = int(input())

        # 테스트케이스 종료
        if not n:
            break

        board = [list(map(int, input().split())) for _ in range(n)]

        # 각 칸에 도착시 잃게되는 금액을 그 칸으로의 간선의 가중치로 생각하여
        # dijkstra's algorithm으로 (0, 0) 으로부터의 최단거리를 구함
        dp = [[INF] * n for _ in range(n)]
        q = [(board[0][0], 0, 0)]
        dp[0][0] = board[0][0]
        while q:
            d, r, c = heappop(q)
            if dp[r][c] < d:
                continue

            # 위
            if r > 0:
                nr, nc = r - 1, c
                nd = dp[r][c] + board[nr][nc]
                if nd < dp[nr][nc]:
                    dp[nr][nc] = nd
                    heappush(q, (nd, nr, nc))
            if r < n - 1:
                nr, nc = r + 1, c
                nd = dp[r][c] + board[nr][nc]
                if nd < dp[nr][nc]:
                    dp[nr][nc] = nd
                    heappush(q, (nd, nr, nc))
            if c > 0:
                nr, nc = r, c - 1
                nd = dp[r][c] + board[nr][nc]
                if nd < dp[nr][nc]:
                    dp[nr][nc] = nd
                    heappush(q, (nd, nr, nc))
            if c < n - 1:
                nr, nc = r, c + 1
                nd = dp[r][c] + board[nr][nc]
                if nd < dp[nr][nc]:
                    dp[nr][nc] = nd
                    heappush(q, (nd, nr, nc))

        answers.append(dp[-1][-1])

    # 테스트케이스별 정답 반환
    return '\n'.join([f'Problem {i + 1}: {answers[i]}' for i in range(len(answers))])
