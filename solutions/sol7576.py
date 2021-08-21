import sys

input = sys.stdin.readline


# 7576 토마토
# bfs로 토마토 익히기 문제
def sol7576():
    m, n = map(int, input().split())
    # 토마토 상태
    tomato = [input().split() for _ in range(n)]

    # BFS 큐
    q = []

    # 익지 않은 토마토 수
    tc = 0

    for i in range(n):
        for j in range(m):
            # 익지 않은 토마토가 있다면 익지 않은 토마토 갯수 증가
            if tomato[i][j] == '0':
                tc += 1
            # 익은 토마토가 있다면 좌표를 BFS 큐에 삽입
            elif tomato[i][j] == '1':
                q.append((i, j))

    # 익지않은 토마토가 없다면 0을 반환 - 이미 다 익어있음
    if tc == 0:
        return 0

    # 익는데 필요한 날짜
    res = 0

    while q:
        nq = []
        for r, c in q:
            # 익은 토마토에 인접한 토마토 중 익지 않은것이 있는 경우
            # 토마토를 익히고 익지 않은 토마토 수를 감소시킨다
            # 만약 익지 않은 토마토의 갯수가 0이된다면 지난 일수 res에 당일을 포함하여 res+1 반환
            # 익은 토마토의 좌표를 큐에 삽입
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < n and 0 <= nc < m and tomato[nr][nc] == '0':
                    tomato[nr][nc] = '1'
                    tc -= 1
                    if tc == 0:
                        return res + 1
                    nq.append((nr, nc))
        # 큐 교체
        q = nq

        # 일수 + 1
        res += 1

    # 큐를 빠져나올 때 까지 익지 않은 토마토 수가 0이 되지 않았다면
    # 모든 토마토를 익힐 수 없는 배치이기 때문에 -1 반환
    return -1
