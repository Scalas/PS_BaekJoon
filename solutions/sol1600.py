import sys

input = sys.stdin.readline


# 1600 말이 되고픈 원숭이
# 원숭이는 n * m 격자판의 (0, 0)에서 (n - 1, m - 1) 로 가려고 하고
# 원숭이는 최대 k번 체스의 나이트처럼 움직일 수 있으며 k번을 모두 쓰고나면 
# 상하좌우로 인접한 칸으로만 이동 가능하며 장애물(1)이 있는 칸으로는 이동 불가능하다고 할 때
# 원숭이가 (n - 1, m - 1)에 도달하기 위해 필요한 이동 횟수의 최솟값을 구하는 문제
def sol1600():
    # 원숭이의 이동방식
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 말의 이동방식
    hdirection = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
    
    k = int(input())
    m, n = map(int, input().split())
    if n == m == 1:
        return 0
    board = [list(map(int, input().split())) for _ in range(n)]

    # bfs로 가장 처음 (n - 1, m - 1)에 도착했을 때의 이동 횟수를 반환
    visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]
    q = [(0, 0, k)]
    answer = 0
    while q:
        nq = []
        answer += 1
        for r, c, cnt in q:
            # 평범한 이동
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if nr == n - 1 and nc == m - 1:
                    return answer
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if board[nr][nc] or visited[nr][nc][cnt]:
                    continue
                visited[nr][nc][cnt] = True
                nq.append((nr, nc, cnt))

            # 말처럼 이동
            if cnt:
                for dr, dc in hdirection:
                    nr, nc = r + dr, c + dc
                    if nr == n - 1 and nc == m - 1:
                        return answer
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    if board[nr][nc] or visited[nr][nc][cnt - 1]:
                        continue
                    visited[nr][nc][cnt - 1] = True
                    nq.append((nr, nc, cnt - 1))
        q = nq

    # bfs 진행중에 (n - 1, m - 1)에 도달하지 못했다면 도달 불가능
    return -1
