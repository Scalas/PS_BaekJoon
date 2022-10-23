import sys

input = sys.stdin.readline


# 21608 상어 초등학교
# n * n 격자공간에 n ** 2 명의 학생을 배치해야한다.
# 학생은 각각 4명의 좋아하는 다른 학생의 번호를 가지고있다.
# 주어진 학생들에게 순서대로 자리를 배치하되, 그 학생이 좋아하는 학생이 인접한 칸에 가장 많은 자리에,
# 그런 칸이 여러개라면 그중 인접한 빈칸이 가장 많은 자리에, 
# 그런 칸도 여러개라면 행이 가장 작은 칸에, 그런 칸도 여러개라면 열이 가장 작은 칸에 배치한다.
# 모든 학생을 배치한 뒤, 각 학생의 만족도는 자신과 인접한 자리의 학생중 좋아하는 학생의 수에 따라
# 0명이면 0, 1명이면 1, 2명이면 10, 3명이면 100, 4명이면 1000이 된다.
# 모든 학생의 만족도의 합을 구하는 문제
def sol21608():
    n = int(input())

    # board[i][j] 는 (i, j) 에 인접한 학생들의 집합
    board = [[set() for _ in range(n)] for _ in range(n)]

    # used[i][j] 는 (i, j)에 배치된 학생의 번호
    used = [[0] * n for _ in range(n)]

    # 빈칸의 갯수를 구하는 함수
    def get_blank_adj(r, c):
        res = 4 - len(board[r][c])
        if r == 0 or r == n - 1:
            res -= 1
        if c == 0 or c == n - 1:
            res -= 1
        return res

    # g[i] 는 i 번 학생이 좋아하는 학생의 집합
    g = [None] * (n ** 2 + 1)

    for _ in range(n ** 2):
        sid, *like = map(int, input().split())
        like = set(like)
        g[sid] = like

        # 인접 set과 like set의 교집합의 길이가 가장 크고
        # 그중에서 빈칸의 갯수가 가장 많은 칸을 구함
        # 같을 경우 업데이트하지 않는 것으로 행, 열 조건 만족
        max_like = -1
        max_blank_adj = -1
        mr, mc = -1, -1
        for i in range(n):
            for j in range(n):
                if used[i][j]:
                    continue
                match = len(board[i][j] & like)
                blank_adj = get_blank_adj(i, j)
                if match > max_like:
                    max_like, max_blank_adj, mr, mc = match, blank_adj, i, j
                elif match == max_like and blank_adj > max_blank_adj:
                    max_blank_adj, mr, mc = blank_adj, i, j

        # 학생을 배치하고 인접 set을 업데이트
        used[mr][mc] = sid
        if mr > 0:
            board[mr - 1][mc].add(sid)
        if mr < n - 1:
            board[mr + 1][mc].add(sid)
        if mc > 0:
            board[mr][mc - 1].add(sid)
        if mc < n - 1:
            board[mr][mc + 1].add(sid)

    # 만족도의 합 계산
    satisfy = [0, 1, 10, 100, 1000]

    return sum([satisfy[len(g[used[i][j]] & board[i][j])] for i in range(n) for j in range(n)])
