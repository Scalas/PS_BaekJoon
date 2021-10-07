import sys
from itertools import combinations

input = sys.stdin.readline


def sol14502():
    # 연구소 크기
    n, m = map(int, input().split())

    # 연구소 상태
    board = [list(map(int, input().split())) for _ in range(n)]

    # 벽을 세울 수 있는 빈 칸들의 좌표 리스트
    wall_slot = []

    # 바이러스의 좌표 리스트
    virus = []

    # wall_slot 과 virus 리스트 채우기
    for i in range(n):
        for j in range(m):
            if not board[i][j]:
                wall_slot.append((i, j))
            elif board[i][j] == 2:
                virus.append((i, j))

    # 빈 칸중 3개를 고르는 모든 경우의 수에 대해
    # 선택된 세 칸에 벽을 세우고 simulate 함수를 호출하여 바이러스가 퍼지게한다
    # 빈칸의 총 갯수 - 바이러스가 추가로 차지한 칸의 갯수 - 세운 벽의 갯수 가 해당 경우의 안전영역의 크기가 된다.
    answer = 0
    for walls in combinations(wall_slot, 3):
        nboard = [board[i][:] for i in range(n)]
        for r, c in walls:
            nboard[r][c] = 1
        answer = max(answer, len(wall_slot) - simulate(nboard, virus, n, m) - 3)

    # 안전 영역의 최대 크기 반환
    return answer


# 바이러스를 실제로 퍼뜨려보는 시뮬레이션 함수
def simulate(board, virus, n, m):
    res = 0
    for r, c in virus:
        res += dfs(board, r, c, n, m)
    return res - len(virus)


# dfs 함수
# 탐색한 칸 수(바이러스가 퍼진 칸 수)를 반환
def dfs(board, r, c, n, m):
    cnt = 1
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 0:
            board[nr][nc] = 2
            cnt += dfs(board, nr, nc, n, m)
    return cnt
