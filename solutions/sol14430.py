import sys

input = sys.stdin.readline


# 14430 자원 캐기
# n * m 격자공간에서 오른쪽 또는 아래쪽으로만 이동하며 자원을 수집할 때
# 얻을 수 있는 최대 자원 수를 구하는 문제
def sol14430():
    n, m = map(int, input().split())
    land = [[*map(int, input().split()), 0] for _ in range(n)]
    land.append([0] * (m+1))
    for i in range(n):
        for j in range(m):
            land[i][j] += max(land[i-1][j], land[i][j-1])

    return land[n-1][m-1]
