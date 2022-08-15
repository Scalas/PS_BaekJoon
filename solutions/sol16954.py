import sys

input = sys.stdin.readline


# 16954 움직이는 미로 탈출
# 8 * 8 미로에 벽의 위치가 주어지고 각 벽이 매 시간마다 한칸씩 아래로 이동할 때
# 맨 왼쪽 아래에서 매 시간마다 가만히 있거나 상하좌우, 대각선으로 인접한 한칸씩 이동하여 맨 오른쪽으로 갈 수 있는지 여부를 구하는 문제
# 단, 이동은 벽이 아닌 칸으로만 가능하며 이동한 후에 벽이 자신에게로 이동하면 더이상 움직일 수 없게 된다.
# 또한 벽은 맨 마지막 행에서 아래로 이동시 사라지게된다.
def sol16954():
    # 벽의 위치
    walls = set()
    for i in range(8):
        line = input().rstrip()
        for j in range(8):
            if line[j] == '#':
                walls.add((i, j))

    # 이동가능 방향
    directions = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (-1, 1), (0, -1), (-1, -1)]

    # bfs로 이동가능한 영역 탐색
    q = [(7, 0)]
    visited = [[0] * 8 for _ in range(8)]
    visited[7][0] = 1
    turn = 1
    while q:
        nq = []
        turn += 1
        for r, c in q:
            # 벽이 현재 위치로 이동했을 경우 더이상 움직일 수 없음
            if (r, c) in walls:
                continue
            for d in range(9):
                nr, nc = r + directions[d][0], c + directions[d][1]
                # 범위를 벗어날 경우
                if not (0 <= nr < 8 and 0 <= nc < 8):
                    continue

                # 벽이 있는 위치일 경우
                if (nr, nc) in walls:
                    continue

                # 이번 턴에 이미 이동한 칸인 경우
                if visited[nr][nc] == turn:
                    continue
                    
                # 목적지에 도착한 경우
                if nr == 0 and nc == 7:
                    return 1

                # 이동 후 방문 처리
                visited[nr][nc] = turn
                nq.append((nr, nc))
        
        # 벽의 이동
        nwalls = set()
        for wr, wc in walls:
            if wr < 7:
                nwalls.add((wr + 1, wc))
        walls = nwalls
        q = nq

    # 마지막 까지 목적지에 도착하지 못했을 경우
    return 0
