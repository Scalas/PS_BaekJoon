import sys

input = sys.stdin.readline


# 1405 미친 로봇
# 로봇이 동서남북 네방향으로 주어진 확률로 이동한다고 할 때
# 로봇이 n번 움직여서 같은자리를 한번도 방문하지 않을 확률을 구하는 문제
def sol1405():
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    n, *rate = map(int, input().split())
    directions = [directions[d] + [d] for d in range(4) if rate[d]]
    rate = [r/100 for r in rate]
    board = [[0] * (n * 2 + 1) for _ in range(n * 2 + 1)]
    board[n][n] = 1

    answer = 0

    def dfs(r, c, visited, cur_rate, count):
        nonlocal answer

        if count == n:
            answer += cur_rate
            return

        for dr, dc, d in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            dfs(nr, nc, visited, cur_rate * rate[d], count + 1)
            visited.remove((nr, nc))

    dfs(n, n, {(n, n)}, 1, 0)

    return answer
