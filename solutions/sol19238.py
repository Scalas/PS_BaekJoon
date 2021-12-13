import sys

input = sys.stdin.readline


# 19238 스타트 택시
# n * n 공간에서 택시의 초기위치 좌표 (tr, tc)와 승객들의 현재위치, 목적지위치의 좌표가 주어졌을 때
# 모든 승객을 목적지에 데려다주고 남은 연료량을 구하는 문제
# 택시는 현재위치에서 가장 가까운 승객(같은 거리라면 행, 열 순으로 오름차순정렬시 맨 처음의 승객)을 우선적으로 태우며
# 승객을 성공적으로 데려다줄 경우 승객의 위치에서 목적지까지의 거리의 두배만큼 연료가 충전된다.
def sol19238():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m, f = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    tr, tc = map(int, input().split())
    tr -= 1
    tc -= 1

    # 승객의 현재위치: 목적지위치
    passenger = dict()
    for i in range(m):
        sr, sc, dr, dc = map(int, input().split())
        board[sr-1][sc-1] = -1
        passenger[(sr-1, sc-1)] = (dr-1, dc-1)

    # 다음 승객의 위치와 택시로부터의 거리를 반환
    def next_passenger(r, c):
        # 택시의 위치에 승객이 있을 경우
        if board[r][c] == -1:
            return [(r, c), 0]

        # 가장 가까이에있는 승객들을 구한다
        q = [(r, c)]
        visited = [[False] * n for _ in range(n)]
        visited[r][c] = True
        dist = 0
        while q:
            dist += 1
            nq = []
            cand = []
            for cr, cc in q:
                for d in directions:
                    nr, nc = cr + d[0], cc + d[1]
                    if not (0 <= nr < n and 0 <= nc < n) or board[nr][nc] == 1:
                        continue

                    if not visited[nr][nc]:
                        if board[nr][nc]:
                            cand.append((nr, nc))
                        else:
                            visited[nr][nc] = True
                            nq.append((nr, nc))
            # 가장 가까이에 있는 승객중 행, 열 순으로 오름차순 정렬하여 맨 처음인 승객이 다음 승객이 된다
            if cand:
                return [min(cand), dist]
            q = nq
        return [0, 0]

    # 데려다준 승객 수
    cnt = 0

    # 연료가 남아있는 동안
    for _ in range(m):
        # 다음 승객 탐색
        src, dist = next_passenger(tr, tc)

        # 태울 수 있는 승객이 없을 경우 운행 종료
        if not src:
            break

        # 승객을 태운다
        board[src[0]][src[1]] = 0

        # 목적지
        dst = passenger[src]

        # 승객에게 이동할 연료가 없는 경우 운행종료
        if f < dist:
            break
        f -= dist

        # 목적지까지의 거리계산
        visited = [[False] * n for _ in range(n)]
        q = [src]
        move = 0
        arrive = False
        while q:
            move += 1
            nq = []
            for r, c in q:
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if dst == (nr, nc):
                        arrive = True
                        break
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        nq.append((nr, nc))
                if arrive:
                    break
            if arrive:
                break
            q = nq

        # 승객을 태우고 목적지까지 가기 위한 연료가 없거나 목적지에 도착할 수 없을 경우 운행종료
        if f < move or not arrive:
            break

        # 택시는 목적지로 이동하고 연료상태 갱신, 데려다준 승객수 증가
        tr, tc = dst
        f += move
        cnt += 1

    # 모든 승객을 데려다줬다면 남은 연료양을, 그러지 못했다면 -1 반환
    return f if cnt == m else -1
