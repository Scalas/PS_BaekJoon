import sys

sys.setrecursionlimit(300000)
input = sys.stdin.readline


# 17090 미로 탈출하기
# n * m 미로의 각 칸의 이동명령이 주어지고(상하좌우)
# 이동 명령에 따라 이동했을 때 미로의 경계밖으로 나갈 수 있는 칸을 탈출 가능한 칸이라 할 때
# 탈출 가능한 칸의 갯수를 구하는 문제
def sol17090():
    n, m = map(int, input().split())
    laby = [input().rstrip() for _ in range(n)]
    d = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

    # escpae[i][j] 는 탈출 가능한 칸이라면 1, 불가능하다면 0, 아직 확인하지 않았다면(초기값) -1
    escape = [[-1] * m for _ in range(n)]

    def dfs(r, c):
        # 경계 밖으로 벗어났다면 탈출 성공 => 1반환
        if not (0 <= r < n and 0 <= c < m):
            return 1
        if escape[r][c] < 0:
            dr, dc = d[laby[r][c]]
            # 현재 칸을 0으로 초기화한 뒤 이동명령에 따라 이동
            # 만약 탈출 불가능한 칸이라면 결국 이미 방문한 칸중 하나로 돌아와 0을 반환하게됨
            escape[r][c] = 0
            escape[r][c] = dfs(r+dr, c+dc)
        return escape[r][c]

    # 탈출 가능한 칸의 갯수를 구하여 반환
    answer = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) > 0:
                answer += 1
    return answer
