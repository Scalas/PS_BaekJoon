import sys

input = sys.stdin.readline


# 2210 숫자판 점프
# 칸마다 0 ~ 9 사이의 수가 적혀진 5 * 5 숫자판의 임의 위치에서 시작하여
# 5번 이동하여 지나간 6개의 숫자를 차례대로 붙여 여섯자리 수를 만들 때
# 만들 수 있는 수의 갯수를 구하는 문제
# 이미 지났던 칸으로도 이동이 가능하다.
def sol2210():
    board = [list(input().split()) for _ in range(5)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    answer = set()

    def dfs(r, c, path):
        if len(path) == 6:
            answer.add(path)
            return

        for dr, dc in directions:
            nr, nc = r + dr , c + dc
            if not (0 <= nr < 5 and 0 <= nc < 5):
                continue
            dfs(nr, nc, path + board[nr][nc])

    for i in range(5):
        for j in range(5):
            dfs(i, j, board[i][j])

    return len(answer)
