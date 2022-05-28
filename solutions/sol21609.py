import sys

input = sys.stdin.readline


# 21609 상어 중학교
# n * n 격자지도에 들어있는 블록의 색이 주어졌을 떄
# 규칙에 따라 블록을 지우고 격자를 회전시키며
# 더이상 블록그룹이 없을 때 까지 반복하여 얻은 점수를 구하는 문제
# 조건:
# 1. 블록 그룹은 2 개 이상의 블록을 포함
# 2. 블록 그룹에는 같은색의 블록들만이 속할 수 있음
# 3. 무지개색 블록은 모든 블록그룹에 속할 수 있으며 검은색은 어느 블록그룹에도 속할 수 없음
# 4. 블록 그룹중 가장 큰 것을 고를 때는 그룹의 크기(블록갯수) -> 무지개색 블록의 갯수 -> 기준블록의 행의 크기 -> 기준블록의 열의 크기 순으로 고려
# 5. 그룹의 기준 블록은 그룹의 블록중 행이 가장작은것 -> 그중 열이 가장 작은것
#
# 절차:
# 1. 크기가 가장 큰 블록 그룹을 찾아 제거하고 그 크기의 제곱만큼 점수를 획득
# 2. 격자에 중력 작용
# 3. 격자를 반시계방향 90도 회전
# 4. 격자에 다시 중력 작용
# 5. 블록 그룹이 존재하지 않으면 게임 종료
def sol21609():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    # bfs 함수
    # (i, j)가 속한 블록 그룹의 크기(가진 블록 갯수), 무지개블록의 수를 반환
    # d가 True일 경우 해당 그룹의 블록 제거
    def bfs(i, j, visited, d):
        q = [(i, j)]
        visited[i][j] = True
        res = [1, 0]
        color = board[i][j]
        if color == 0:
            res[1] += 1
        if d:
            board[i][j] = -2
        rainbow = []
        while q:
            nq = []
            for r, c in q:
                if r > 0:
                    nr, nc = r - 1, c
                    if not visited[nr][nc] and (board[nr][nc] == color or board[nr][nc] == 0):
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                        res[0] += 1
                        if board[nr][nc] == 0:
                            res[1] += 1
                            rainbow.append((nr, nc))
                        if d:
                            board[nr][nc] = -2
                if r < n - 1:
                    nr, nc = r + 1, c
                    if not visited[nr][nc] and (board[nr][nc] == color or board[nr][nc] == 0):
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                        res[0] += 1
                        if board[nr][nc] == 0:
                            res[1] += 1
                            rainbow.append((nr, nc))
                        if d:
                            board[nr][nc] = -2
                if c > 0:
                    nr, nc = r, c - 1
                    if not visited[nr][nc] and (board[nr][nc] == color or board[nr][nc] == 0):
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                        res[0] += 1
                        if board[nr][nc] == 0:
                            res[1] += 1
                            rainbow.append((nr, nc))
                        if d:
                            board[nr][nc] = -2
                if c < n - 1:
                    nr, nc = r, c + 1
                    if not visited[nr][nc] and (board[nr][nc] == color or board[nr][nc] == 0):
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                        res[0] += 1
                        if board[nr][nc] == 0:
                            res[1] += 1
                            rainbow.append((nr, nc))
                        if d:
                            board[nr][nc] = -2
            q = nq

        # 무지개 블록 방문 초기화
        for r, c in rainbow:
            visited[r][c] = False

        return res

    # 가장 큰 블록 그룹 부수기
    def destroy():
        visited = [[False] * n for _ in range(n)]
        cand = []
        for i in range(n):
            for j in range(n):
                if board[i][j] <= 0:
                    continue
                if not visited[i][j]:
                    group = bfs(i, j, visited, False)
                    if group[0] >= 2:
                        cand.append([group, i, j])

        # 후보 블록이 없다면
        if not cand:
            return 0

        # 후보블록중 우선순위가 가장 높은 것을 파괴
        target = max(cand)
        return bfs(target[1], target[2], [[False] * n for _ in range(n)], True)[0]

    # 격자에 중력 작용
    def gravity():
        for j in range(n):
            # 위에서부터 떨어져야할 블록들 탐색
            drop = []
            i = 0
            while i < n:
                # 검은 블록을 제외한 블록들을 drop에 삽입
                # 떨어져야할 블록이 있던 칸은 빈칸으로
                if board[i][j] >= 0:
                    drop.append(board[i][j])
                    board[i][j] = -2

                # 검은 블록을 만나면 검은블록까지만 떨어짐
                # drop 리스트 초기화
                elif board[i][j] == -1:
                    for k in range(len(drop)):
                        board[i-k-1][j] = drop[len(drop)-k-1]
                    drop = []
                i += 1

            # 밑바닥으로 떨어질 블록 처리
            if drop:
                for k in range(len(drop)):
                    board[n-k-1][j] = drop[len(drop)-k-1]

    # 반시계방향 90도 회전
    def rotate():
        nonlocal board
        new_board = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_board[i][j] = board[j][n-i-1]
        board = new_board

    score = 0
    while True:
        # 가장 큰 블록 그룹을 탐색하여 제거, 제거된 블록 갯수의 제곱만큼 점수획득
        # 만약 부술 블록그룹이 더이상 존재하지 않는다면 오토플레이 종료
        achieved = destroy()
        if not achieved:
            break
        score += achieved ** 2

        # 격자에 중력 작용
        gravity()

        # 반시계방향 90도 회전
        rotate()

        # 격자에 중력 작용
        gravity()

    # 점수 반환
    return score
