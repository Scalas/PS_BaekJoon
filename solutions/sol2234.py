import sys

input = sys.stdin.readline


# 2234 성곽
# 각 칸의 좌 상 우 하 방향의 벽의 유무가 표시된 격자공간이 2차원 리스트가 주어졌을 때
# 방의 갯수, 가장 큰 방의 크기, 벽을 하나 부쉈을 때 가능한 가장 큰 방의 크기를 구하는 문제
def sol2234():
    direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    bit = [1, 2, 4, 8]
    m, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]

    # 방 번호
    room = 0

    # 방 크기 리스트
    size_list = []

    # bfs로 각 칸의 소속 방 번호를 표시하며 크기를 측정
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 0:
                continue
            q = [(i, j)]
            visited[i][j] = room
            size = 1
            while q:
                nq = []
                for ci, cj in q:
                    state = board[ci][cj]
                    for k in range(4):
                        if not (state & bit[k]):
                            ni, nj = ci + direction[k][0], cj + direction[k][1]
                            if visited[ni][nj] < 0:
                                visited[ni][nj] = room
                                nq.append((ni, nj))
                                size += 1
                q = nq
            room += 1
            size_list.append(size)

    # 단일 방 최대 크기
    max_room = max(size_list)

    # 인접한 두 칸끼리 방번호가 다를 경우에만 두 방의 크기를 더한 값으로 벽을 부쉈을 때의 최대 방 크기를 갱신
    exp = max_room
    for i in range(n):
        for j in range(m):
            state = board[i][j]
            for k in range(4):
                if not state & bit[k]:
                    continue
                ni, nj = i + direction[k][0], j + direction[k][1]
                if not (0 <= ni < n and 0 <= nj < m):
                    continue
                if visited[ni][nj] != visited[i][j]:
                    exp = max(exp, size_list[visited[ni][nj]] + size_list[visited[i][j]])
    return '\n'.join(map(str, [room, max_room, exp]))
