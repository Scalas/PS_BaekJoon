import sys

input = sys.stdin.readline


# 2178 미로탐색
# 마지막칸에 가기위한 최단거리 구하기
# 전형적인 bfs 문제
def sol2178():
    n, m = map(int, input().split())
    # 미로
    laby = [list(input().rstrip()) for _ in range(n)]

    # 시작 위치
    q = [(0, 0)]

    # 사이클 수
    cnt = 1

    while q:
        nq = []
        for r, c in q:
            # 현재 위치가 이미 방문된 상태일 경우 continue
            if laby[r][c] != '1':
                continue

            # 현재 시점의 사이클 수 = 최단거리 로 갱신
            laby[r][c] = cnt

            # 인접 위치중 아직 방문하지 않았으며 갈 수 있는 위치를 큐에 삽입
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0<=nr<n and 0<=nc<m and laby[nr][nc]=='1':
                    nq.append((nr, nc))

        # 다음 사이클을 위한 큐로 교체
        q = nq

        # 사이클 수 증가
        cnt += 1

    # n, m까지의 최단거리 반환 (인덱스가 0부터 시작하도록 구현했기에 n-1, m-1)
    return laby[n-1][m-1]
