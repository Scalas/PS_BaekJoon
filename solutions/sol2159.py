import sys

input = sys.stdin.readline
INF = 10 ** 12


# 2159 케잌 배달
# 100000 * 100000 격자공간에 레스토랑의 좌표와 n명의 손님의 좌표가 주어지고
# 주어진 좌표 순서대로 손님에게 케잌을 배달하려 할 때 이동 경로의 최단거리를 구하는 문제
# 단, 손님에게 케잌을 배달하려면 손님의 위치 또는 상하좌우로 인접한 위치로 가야하며
# 지나가는길에 순서에 맞지않는 손님에게 케잌을 배달할 수 있는 장소에 가더라도 케잌은 배달하지 않는다.
def sol2159():
    directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    n = int(input())

    # 레스토랑 위치
    sr, sc = map(int, input().split())
    clients = [(sr, sc)]

    # 레스토랑과 첫 손님까지의 케이스별 최단거리
    dp = [[INF] * 5 for _ in range(n + 1)]
    for i in range(5):
        dp[0][i] = 0
    u, v = map(int, input().split())
    for i in range(5):
        cr, cc = u + directions[i][0], v + directions[i][1]
        dp[1][i] = abs(cr - sr) + abs(cc - sc)
    clients.append((u, v))

    # 각 손님으로의 최단거리
    for i in range(2, n + 1):
        u, v = map(int, input().split())

        # i번 손님에게 케잌을 배달할 수 있는 위치마다 최단거리를 구함

        # 손님의 위치에 케잌배달시
        cr, cc = u, v
        dst = INF
        for j in range(5):
            pr, pc = clients[-1][0] + directions[j][0], clients[-1][1] + directions[j][1]
            dst = min(dst, dp[i - 1][j] + abs(cr - pr) + abs(cc - pc))
        dp[i][0] = dst

        # 손님의 왼쪽 위치에 케잌배달시
        if u > 0:
            cr, cc = u - 1, v
            dst = INF
            for j in range(5):
                pr, pc = clients[-1][0] + directions[j][0], clients[-1][1] + directions[j][1]
                dst = min(dst, dp[i - 1][j] + abs(cr - pr) + abs(cc - pc))
            dp[i][1] = dst

        # 손님의 오른쪽 위치에 케잌배달시
        if u < 100000:
            cr, cc = u + 1, v
            dst = INF
            for j in range(5):
                pr, pc = clients[-1][0] + directions[j][0], clients[-1][1] + directions[j][1]
                dst = min(dst, dp[i - 1][j] + abs(cr - pr) + abs(cc - pc))
            dp[i][2] = dst

        # 손님의 아래쪽 위치에 케잌배달시
        if v > 0:
            cr, cc = u, v - 1
            dst = INF
            for j in range(5):
                pr, pc = clients[-1][0] + directions[j][0], clients[-1][1] + directions[j][1]
                dst = min(dst, dp[i - 1][j] + abs(cr - pr) + abs(cc - pc))
            dp[i][3] = dst

        # 손님의 위쪽 위치에 케잌배달시
        if v < 100000:
            cr, cc = u, v + 1
            dst = INF
            for j in range(5):
                pr, pc = clients[-1][0] + directions[j][0], clients[-1][1] + directions[j][1]
                dst = min(dst, dp[i - 1][j] + abs(cr - pr) + abs(cc - pc))
            dp[i][4] = dst
        clients.append((u, v))

    # 마지막 손님에게 케잌을 배달한 경우중 최단거리 반환
    return min(dp[-1])
