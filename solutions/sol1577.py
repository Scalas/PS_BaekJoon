import sys

input = sys.stdin.readline


# 1577 도로의 갯수
# k개의 도로가 공사중이라 지나갈 수 없는 상태인 n, m 격자공간의
# (0, 0) 에서 (n, m)으로 최단거리(n + m)로만 이동할 때
# (n, m)에 도착 가능한 서로 다른 경로의 수를 구하는 문제
def sol1577():
    n, m = map(int, input().split())
    blocked = set()

    # 차단된 경로
    for _ in range(int(input())):
        r1, c1, r2, c2 = map(int, input().split())
        if r1 > r2 or (r1 == r2 and c1 > c2):
            r1, c1, r2, c2 = r2, c2, r1, c1
        blocked.add((r1, c1, r2, c2))

    # path[i][j] 는 (0, 0) 에서 (i, j)로 가는 서로 다른 경로의 수
    path = [[0] * (m + 1) for _ in range(n + 1)]
    path[0][0] = 1
    for i in range(1, n + 1):
        if (i - 1, 0, i, 0) in blocked:
            break
        path[i][0] = 1

    for i in range(1, m + 1):
        if (0, i - 1, 0, i) in blocked:
            break
        path[0][i] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j > 0 and (i, j - 1, i, j) not in blocked:
                path[i][j] += path[i][j - 1]

            if i > 0 and (i - 1, j, i, j) not in blocked:
                path[i][j] += path[i - 1][j]

    return path[n][m]
