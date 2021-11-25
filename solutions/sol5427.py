import sys

input = sys.stdin.readline


# 5427 불
# 매 초마다 인접한 빈 공간에 불이 옮겨붙는 건물에서 탈출하는데 걸리는 시간을 구하는 문제
def sol5427():
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = []
    for _ in range(int(input())):
        w, h = map(int, input().split())
        board = [list(input().rstrip()) for _ in range(h)]
        sx, sy = 0, 0
        q = []
        for i in range(h):
            for j in range(w):
                if board[i][j] == '@':
                    sx, sy = i, j
                    board[i][j] = '.'
                elif board[i][j] == '*':
                    q.append((i, j))
                    board[i][j] = 0

        # 초당 불이 퍼져나가는 상태를 기록
        time = 0
        while q:
            time += 1
            nq = []
            for r, c in q:
                for d in direction:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < h and 0 <= nc < w and board[nr][nc] == '.':
                        board[nr][nc] = time
                        nq.append((nr, nc))
            q = nq

        # 탈출 시도
        q = [(sx, sy)]
        visited = [[False] * w for _ in range(h)]
        visited[sx][sy] = True
        time = 0
        res = False
        while q:
            time += 1
            nq = []
            for r, c in q:
                for d in direction:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < h and 0 <= nc < w:
                        if not visited[nr][nc] and board[nr][nc] != '#' and (board[nr][nc] == '.' or board[nr][nc] > time):
                            visited[nr][nc] = True
                            nq.append((nr, nc))
                    else:
                        answer.append(str(time))
                        res = True
                        break
                if res:
                    break
            if res:
                break
            q = nq
        if not res:
            answer.append('IMPOSSIBLE')
    return '\n'.join(answer)
