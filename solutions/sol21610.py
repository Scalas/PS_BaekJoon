import sys

input = sys.stdin.readline


# 21610 마법사 상어와 비바라기
# 처음 왼쪽 아래 2 * 2 크기의 구름이 있는 상태로 시작
# 매턴 구름이 이동 후 비가내려 구름이 있던칸에 물 1씩 증가
# 물이 증가한 칸의 대각선방향에 물이 있을때마다 1씩 물이 증가
# 비가 내리지 않은 칸중 물이 2 이상인 곳에서 구름 생성
# 이를 반복하여 m번 이동이 완료된 후 남은 물의 총합을 구하는 문제
def sol21610():
    directions = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 구름의 리스트
    cloud = [(n - 2, 0), (n - 1, 0), (n - 2, 1), (n - 1, 1)]

    # m번의 이동
    turn = 0
    for _ in range(m):
        turn += 1

        d, s = map(int, input().split())
        visited = set()

        # 구름 이동 후 강수
        for r, c in cloud:
            direction = directions[d]
            nr, nc = (r + direction[0] * s) % n, (c + direction[1] * s) % n
            board[nr][nc] += 1
            visited.add((nr, nc))

        # 물복사
        for nr, nc in visited:
            for nd in range(2, 9, 2):
                ar, ac = nr + directions[nd][0], nc + directions[nd][1]
                if not (0 <= ar < n and 0 <= ac < n):
                    continue

                if board[ar][ac]:
                    board[nr][nc] += 1

        # 새 구름 생성
        ncloud = []
        for i in range(n):
            for j in range(n):
                if (i, j) in visited:
                    continue
                if board[i][j] >= 2:
                    ncloud.append((i, j))
                    board[i][j] -= 2

        cloud = ncloud

    return sum([sum(line) for line in board])
