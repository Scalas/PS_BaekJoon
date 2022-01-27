import sys

input = sys.stdin.readline


# 2186 문자판
# n * m 칸으로 이루어진 문자판의 각 칸에는 알파벳 대문자가 쓰여있고
# 문자판 내의 임의의 칸에서 시작하여 상하좌우로 최대 k번 이동 가능하다.(한번 지나간 칸도 다시 지날수있다)
# 이 때, 지나간 칸의 알파벳으로 주어진 문자열을 만들 수 있는 경로의 수를 구하는 문제
def sol2186():
    n, m, k = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    word = input().rstrip()
    lw = len(word)

    # 이동가능한 방식
    direction = []
    for i in range(1, k+1):
        direction.append((-i, 0))
        direction.append((i, 0))
        direction.append((0, i))
        direction.append((0, -i))

    dp = [[[-1] * lw for _ in range(m)] for _ in range(n)]

    def dfs(r, c, idx):
        if dp[r][c][idx] < 0:
            res = 0
            # 마지막 문자일 경우
            if idx == lw-1:
                res = 1

            # 마지막 문자가 아닐 경우
            else:
                # 이동 가능한 방향과 거리로
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    # 이동한 칸이 문자판 내에 존재하며 단어의 다음문자와 일치할 경우
                    if 0 <= nr < n and 0 <= nc < m:
                        if board[nr][nc] == word[idx+1]:
                            res += dfs(nr, nc, idx+1)
            dp[r][c][idx] = res
        return dp[r][c][idx]

    answer = 0
    for i in range(n):
        for j in range(m):
            # 단어의 첫 문자와 일치하는 칸을 시작으로 하여 탐색
            if board[i][j] == word[0]:
                answer += dfs(i, j, 0)
    return answer
