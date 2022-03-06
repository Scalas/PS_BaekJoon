import sys

input = sys.stdin.readline


# 2589 보물섬
# 땅은 L, 바다는 W로 표시된 n * m 크기의 보물섬 지도가 주어지고
# 육지상에서 서로간의 최단거리가 가장 먼 두 곳에 보물이 숨겨져있을 때
# 보물이 숨겨진 두 지역 사이의 거리를 구하는 문제
def sol2589():
    n, m = map(int, input().split())
    board = [input().rstrip() for _ in range(n)]

    # bfs를 사용한 최단거리의 최댓값을 모든 육지에 대해 구하고
    # 그 값중 최댓값을 구하면 해결 가능
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'L':
                visited = [[False] * m for _ in range(n)]
                q = [(i, j)]
                visited[i][j] = True
                cnt = -1
                while q:
                    cnt += 1
                    nq = []
                    for r, c in q:
                        if r > 0:
                            nr, nc = r-1, c
                            if not visited[nr][nc] and board[nr][nc] == 'L':
                                visited[nr][nc] = True
                                nq.append((nr, nc))
                        if r < n-1:
                            nr, nc = r+1, c
                            if not visited[nr][nc] and board[nr][nc] == 'L':
                                visited[nr][nc] = True
                                nq.append((nr, nc))
                        if c > 0:
                            nr, nc = r, c-1
                            if not visited[nr][nc] and board[nr][nc] == 'L':
                                visited[nr][nc] = True
                                nq.append((nr, nc))
                        if c < m-1:
                            nr, nc = r, c+1
                            if not visited[nr][nc] and board[nr][nc] == 'L':
                                visited[nr][nc] = True
                                nq.append((nr, nc))
                    q = nq
                answer = max(answer, cnt)
    return answer
