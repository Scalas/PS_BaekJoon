import sys
from itertools import combinations

input = sys.stdin.readline
INF = 10 ** 9


# 17142 연구소 3
# n * n 크기의 연구소의 m개 이상 10개 이하의 바이러스가 존재하고
# 그중 m개를 활성화시키면 1초마다 상하좌우로 인접한 한칸씩 바이러스가 퍼진다고 할 때
# 활성화 시킬 m개의 바이러스를 선택하여 바이러스가 연구소 전체에 퍼지게 하기위한 최소 시간을 구하는 문제
# 만약 어떻게 해도 바이러스를 모두 퍼트릴 수 없다면 -1을 반환
def sol17142():
    n, m = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(n)]

    # 바이러스의 좌표 리스트와 빈칸의 갯수를 구함
    virus = []
    empty = 0
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 2:
                virus.append((i, j))
            elif lab[i][j] == 0:
                empty += 1

    # 바이러스의 좌표 리스트중 m개를 고르는 모든 경우의 수에 대해 바이러스를 퍼트리는데 걸리는 시간을 측정
    # 그 중 최솟값을 구하여 반환
    activate_cases = list(map(list, combinations(virus, m)))
    answer = INF
    for case in activate_cases:
        visited = [[False] * n for _ in range(n)]
        q = case
        remain = empty
        time = 0
        while q and remain:
            time += 1
            if time >= answer:
                remain = -1
                break
            nq = []
            for r, c in q:
                if r > 0:
                    nr, nc = r - 1, c
                    if not visited[nr][nc] and lab[nr][nc] != 1:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                        if lab[nr][nc] == 0:
                            remain -= 1
                if r < n - 1:
                    nr, nc = r + 1, c
                    if not visited[nr][nc] and lab[nr][nc] != 1:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                        if lab[nr][nc] == 0:
                            remain -= 1
                if c > 0:
                    nr, nc = r, c - 1
                    if not visited[nr][nc] and lab[nr][nc] != 1:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                        if lab[nr][nc] == 0:
                            remain -= 1
                if c < n - 1:
                    nr, nc = r, c + 1
                    if not visited[nr][nc] and lab[nr][nc] != 1:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                        if lab[nr][nc] == 0:
                            remain -= 1
            q = nq

        if not remain:
            answer = min(answer, time)

    return -1 if answer == INF else answer
