import sys

input = sys.stdin.readline


# 3197
def sol3197():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 클러스터를 나누기 위한 bfs 함수
    # 초기 상태에서 서로 이어져있는 물이 있는 공간을 하나의 클러스터로 표시
    def bfs(r, c, cid):
        q = [(r, c)]
        while q:
            nq = []
            for cr, cc in q:
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    if board[nr][nc] != '.':
                        continue
                    board[nr][nc] = cid
                    nq.append((nr, nc))
            q = nq

    # 백조가 있는 좌표와 물이 있는 위치의 좌표를 구함
    swan = []
    q = []
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'L':
                swan.append((i, j))
                board[i][j] = '.'
                q.append((i, j))
                visited[i][j] = True
            elif board[i][j] == '.':
                q.append((i, j))
                visited[i][j] = True

    # 클러스터 분류
    cluster_id = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                board[i][j] = cluster_id
                bfs(i, j, cluster_id)
                cluster_id += 1

    # 매일 두 백조가 만날 수 있는지 검사(find)하여 만날 수 있다면 지난 일 수(answer)를 반환
    # 만날 수 없다면 1일을 진행하고 얼음이 녹음
    # 녹은 얼음과 맞닿아있던 클러스터끼리는 병합이 발생(union)
    cluster = [-1] * cluster_id
    s1, s2 = board[swan[0][0]][swan[0][1]], board[swan[1][0]][swan[1][1]]
    answer = 0
    while q:
        if find(cluster, s1) == find(cluster, s2):
            return answer
        answer += 1
        nq = []
        for cr, cc in q:
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if board[nr][nc] != 'X':
                    continue
                board[nr][nc] = board[cr][cc]

                merged = []
                for adr, adc in directions:
                    ar, ac = nr + adr, nc + adc
                    if not (0 <= ar < n and 0 <= ac < m):
                        continue
                    if board[ar][ac] == 'X':
                        continue
                    merged.append(board[ar][ac])

                for i in range(len(merged) - 1):
                    union(cluster, merged[i], merged[i + 1])

                nq.append((nr, nc))
        q = nq


def union(u, a, b):
    a = find(u, a)
    b = find(u, b)

    if a != b:
        if u[a] < u[b]:
            u[a] += u[b]
            u[b] = a
        else:
            u[b] += u[a]
            u[a] = b


def find(u, x):
    if u[x] < 0:
        return x
    u[x] = find(u, u[x])
    return u[x]
