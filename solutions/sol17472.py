import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float('inf')


# 17472 다리 만들기 2
# 격자보드의 인접한 칸들을 하나의 섬으로 보고 두 섬의 사이에 길이 2 이상의 직선다리를 놓을 떄,
# 모든 섬을 연결하며 다리 길이의 합을 최소로하여 건설했을 때의 다리 길이의 총합을 구하는 문제
# MST 문제이지만 섬 사이의 간선을 구하는게 고역이었던 문제
# dfs를 사용하여 섬을 구분하고 N * M 반복문을 돌려 두 섬 사이의 최단거리를 갱신
def sol17472():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 인접한 칸을 탐색하기 위한 dfs 함수
    def dfs(r, c, land_num):
        board[r][c] = land_num
        for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 1:
                dfs(nr, nc, land_num)

    # 인접한 칸들을 찾아 하나의 섬으로 구분
    # 기존의 0, 1과 구별하기 위해 섬 번호를 2부터 시작
    ln = 2
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                dfs(i, j, ln)
                ln += 1

    g = [[INF] * (ln - 2) for _ in range(ln - 2)]
    # 가로방향으로 섬 사이의 거리의 최솟값을 갱신
    for i in range(n):
        cur, curi = 0, 0
        for j in range(m):
            # 현재칸이 육지인 경우
            if board[i][j] > 0:
                # 기존 섬의 끝 인덱스 갱신
                if board[i][j] == cur:
                    curi = j

                # 새로운 섬을 찾은 경우
                else:
                    # 기존에 찾아둔 섬이 있고, 기존의 섬과 새로운 섬의 거리가 2이상일 경우 섬 사이의 거리를 갱신
                    if cur != 0:
                        if 2 <= j - curi - 1 < g[board[i][j] - 2][cur - 2]:
                            g[board[i][j] - 2][cur - 2] = g[cur - 2][board[i][j] - 2] = j - curi - 1
                    # 새로운 섬의 기존 섬이 된다.
                    cur, curi = board[i][j], j

    # 위 과정을 세로방향으로 반복
    for j in range(m):
        cur, curi = 0, 0
        for i in range(n):
            if board[i][j] > 0:
                if board[i][j] == cur:
                    curi = i
                else:
                    if cur != 0:
                        if 2 <= i - curi - 1 < g[board[i][j] - 2][cur - 2]:
                            g[board[i][j] - 2][cur - 2] = g[cur - 2][board[i][j] - 2] = i - curi - 1
                    cur, curi = board[i][j], i

    # Prim 알고리즘으로 최소신장트리 탐색
    visit = [False] * (ln - 2)
    q = [(0, 0)]
    cnt = 0
    cost = 0
    while q:
        d, adj = heappop(q)
        if not visit[adj]:
            visit[adj] = True
            cost += d
            cnt += 1
            if cnt == ln - 2:
                break
            for next_node in range(ln - 2):
                if not visit[next_node] and g[adj][next_node] != INF:
                    heappush(q, (g[adj][next_node], next_node))
    if cnt < ln - 2:
        return -1
    else:
        return cost