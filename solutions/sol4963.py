import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


# 4963 섬의 개수
# 주어진 격자형 지도에서 1은 땅, 0은 바다라고 할때
# 상하좌우 또는 대각선으로 인접한 땅끼리 이어진 섬의 갯수를 구하는 문제
def sol4963():
    # dfs 나 bfs 를 사용하여 간단히 해결 가능하지만 상하좌우 말고도 대각선 4곳을 추가적으로 탐색해야한다.
    direction = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]

    def dfs(r, c):
        land[r][c] = '0'
        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and land[nr][nc] == '1':
                dfs(nr, nc)

    answer = []
    while True:
        w, h = map(int, input().split())
        if w == h == 0:
            break
        land = [input().split() for _ in range(h)]
        cnt = 0
        for i in range(h):
            for j in range(w):
                if land[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        answer.append(cnt)
    return '\n'.join(map(str, answer))
