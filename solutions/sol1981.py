import sys

input = sys.stdin.readline
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 1981 배열에서 이동
# n * n 배열에서 상하좌우로 인접한 칸으로 이동 가능하며
# (0, 0)에서 (n-1, n-1)로 이동하려고 할 때
# 이동중에 지나간 칸에 써있던 숫자들중 가장 큰 값과 가장 작은 값의 차의 최솟값을 구하는 문제
def sol1981():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_val = max(map(max, board))
    minv, maxv = board[0][0], board[-1][-1]
    if minv > maxv:
        minv, maxv = maxv, minv

    # min_bound에서 max_bound 사이의 수만을 지나며
    # (0, 0)에서 (n-1, n-1)로 갈 수 있는지 검증
    def bfs(minb, maxb):
        visited = [[False] * n for _ in range(n)]
        q = [(0, 0)]
        visited[0][0] = True
        while q:
            nq = []
            for r, c in q:
                if r > 0:
                    nr, nc = r-1, c
                    if minb <= board[nr][nc] <= maxb and not visited[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                if r < n-1:
                    nr, nc = r+1, c
                    if minb <= board[nr][nc] <= maxb and not visited[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                if c > 0:
                    nr, nc = r, c-1
                    if minb <= board[nr][nc] <= maxb and not visited[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                if c < n-1:
                    nr, nc = r, c+1
                    if minb <= board[nr][nc] <= maxb and not visited[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
            q = nq
        return visited[-1][-1]

    answer = 201
    # 최댓값의 범위는 반드시 지나야하는 칸인 (0, 0), (n-1, n-1)중
    # 최댓값 maxv 이상이며 모든 칸중 최댓값인 max_val 이하
    for max_bound in range(maxv, max_val+1):
        s, e = 0, max_bound
        while s <= e:
            # 중간지점을 최댓값-최솟값의 한계치로 지정
            limit = (s + e) // 2

            # 최솟값 한계
            min_bound = max_bound-limit

            # 최솟값 한계가 반드시 지나야하는 칸인 (0, 0), (n-1, n-1)중
            # 최솟값이 minv 보다 크다면 실패가 확정
            if min_bound > minv:
                s = limit+1
                continue

            # 최댓값-최솟값 한계치가 이미 검증된 수치보다 크다면
            # 결과에 상관없이 답이 될 수 없음
            if limit > answer:
                e = limit-1
                continue
            res = bfs(min_bound, max_bound)
            if res:
                answer = min(answer, limit)
                e = limit-1
            else:
                s = limit+1

    # 가능한 최댓값-최솟값의 최솟값 반환
    return answer
