import sys

input = sys.stdin.readline


# 1726 로봇
# n * m 격자공간에서 로봇의 위치와 현재 방향, 최종적으로 도착해야할 위치와 바라봐야할 방향이 주어질 때
# 이를 달성하기 위한 최소 명령 횟수를 구하는 문제
# 명령의 종류는 다음과 같음
# 1. 현재 보고있는 방향으로 1~3칸 이동(도중에 장애물로 막힐 경우 이동 불가)
# 2. 현재 방향에서 좌, 우로 90도 회전
def sol1726():
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 시작위치, 도착위치
    sr, sc, sd = map(lambda x: int(x) - 1, input().split())
    er, ec, ed = map(lambda x: int(x) - 1, input().split())

    # 시작부터 도착위치와 방향을 만족하는 경우
    if sr == er and sc == ec and sd == ed:
        return 0

    # bfs로 최소 명령 횟수 탐색
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    q = [(sr, sc, sd)]
    answer = 0
    while q:
        nq = []
        for r, c, d in q:
            # 목적위치 도착시 명령횟수 반환
            if r == er and c == ec and d == ed:
                return answer

            # 이동
            # 현재 바라보고있는 방향으로 최대 3칸까지 이동
            # 도중에 이동 불가능해질 경우 이동을 멈춤
            # 이미 방문한 칸은 스킵
            dr, dc = direction[d]
            for k in range(1, 4):
                nr, nc = r + dr * k, c + dc * k
                if not (0 <= nr < n and 0 <= nc < m):
                    break
                if board[nr][nc]:
                    break
                if visited[nr][nc][d]:
                    continue
                visited[nr][nc][d] = True
                nq.append((nr, nc, d))

            # 회전
            # 동/서 였으면 남/북으로
            # 남/북 이었으면 동/서로 회전
            if d <= 1:
                if not visited[r][c][2]:
                    nq.append((r, c, 2))
                    visited[r][c][2] = True
                if not visited[r][c][3]:
                    nq.append((r, c, 3))
                    visited[r][c][3] = True
            else:
                if not visited[r][c][0]:
                    nq.append((r, c, 0))
                    visited[r][c][0] = True
                if not visited[r][c][1]:
                    nq.append((r, c, 1))
                    visited[r][c][1] = True
        q = nq
        answer += 1
