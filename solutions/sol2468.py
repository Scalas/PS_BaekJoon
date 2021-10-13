import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


# 2468 안전 영역
# 수위에 따라 달라지는 물에 잠기지 않는 영역의 갯수중 최댓값을 구하는 문제
def sol2468():
    n = int(input())
    land = [list(map(int, input().split())) for _ in range(n)]
    answer = 1
    for wl in range(1, 101):
        visited = [[False] * n for _ in range(n)]
        cnt = 0
        for r in range(n):
            for c in range(n):
                if not visited[r][c] and land[r][c] > wl:
                    dfs(land, visited, n, r, c, wl)
                    cnt += 1
        if not cnt:
            break
        answer = max(answer, cnt)

    return answer


def dfs(land, visited, n, r, c, wl):
    visited[r][c] = True
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if 0 <= nr < n and 0 <= nc < n and land[nr][nc] > wl and not visited[nr][nc]:
            dfs(land, visited, n, nr, nc, wl)
