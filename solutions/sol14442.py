import sys

input = sys.stdin.readline


# 14442 벽 부수고 이동하기 2
# n * m 격자 미로에서 최대 k번까지 벽을 부수고 이동할 수 있을 때
# 미로의 시작(0, 0)에서 끝(n-1, m-1)로 가기 위한 최단거리를 구하는 문제
def sol14442():
    n, m, k = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(n)]

    # 미로의 크기가 1 * 1이라면 시작부터 미로 끝에 서있음
    if n == m == 1:
        return 1

    # visited[i][j] 는 (i, j)에 도착했을 때 남아있는 벽을 부술 수 있는 최대 횟수
    visited = [[-1] * m for _ in range(n)]

    # 시작 지점부터 탐색 시작
    q = [(0, 0)]
    visited[0][0] = k
    answer = 1
    while q:
        # 이동횟수 1 증가
        answer += 1
        nq = []
        for r, c in q:
            # 현재 벽을 부술 수 있는 횟수는 visited[r][c]
            cnt = visited[r][c]

            # 위쪽
            if r > 0:
                nr, nc = r - 1, c
                # 벽을 부술 수 있는 횟수를 기존보다 많이 보존한 채로 이동 가능할 경우
                if cnt > visited[nr][nc]:
                    # 벽으로 막혀있는 경우
                    if board[nr][nc]:
                        # 벽을 부수고 이동해도 벽을 부술 수 있는 횟수를 기존보다 많이 보존한 채로 이동 가능할 경우
                        if cnt - 1 > visited[nr][nc]:
                            # 미로의 끝에 도달
                            if nr == n - 1 and nc == m - 1:
                                return answer

                            # visited를 갱신하고 이동한 위치를 큐에 삽입
                            visited[nr][nc] = cnt - 1
                            nq.append((nr, nc))

                    # 막혀있지 않은 경우
                    else:
                        # 미로의 끝에 도달
                        if nr == n - 1 and nc == m - 1:
                            return answer

                        # visited를 갱신하고 이동한 위치를 큐에 삽입
                        visited[nr][nc] = cnt
                        nq.append((nr, nc))

            # 이하 위의 과정을 아래, 왼쪽, 오른쪽에 대해 반복
            if r < n - 1:
                nr, nc = r + 1, c
                if cnt > visited[nr][nc]:
                    if board[nr][nc]:
                        if cnt - 1 > visited[nr][nc]:
                            if nr == n - 1 and nc == m - 1:
                                return answer
                            visited[nr][nc] = cnt - 1
                            nq.append((nr, nc))
                    else:
                        if nr == n - 1 and nc == m - 1:
                            return answer
                        visited[nr][nc] = cnt
                        nq.append((nr, nc))
            if c > 0:
                nr, nc = r, c - 1
                if cnt > visited[nr][nc]:
                    if board[nr][nc]:
                        if cnt - 1 > visited[nr][nc]:
                            if nr == n - 1 and nc == m - 1:
                                return answer
                            visited[nr][nc] = cnt - 1
                            nq.append((nr, nc))
                    else:
                        if nr == n - 1 and nc == m - 1:
                            return answer
                        visited[nr][nc] = cnt
                        nq.append((nr, nc))
            if c < m - 1:
                nr, nc = r, c + 1
                if cnt > visited[nr][nc]:
                    if board[nr][nc]:
                        if cnt - 1 > visited[nr][nc]:
                            if nr == n - 1 and nc == m - 1:
                                return answer
                            visited[nr][nc] = cnt - 1
                            nq.append((nr, nc))
                    else:
                        if nr == n - 1 and nc == m - 1:
                            return answer
                        visited[nr][nc] = cnt
                        nq.append((nr, nc))
        q = nq

    # 탐색을 마치고도 최단거리를 찾지 못한 경우 끝에 도달할 수 없음
    return -1
