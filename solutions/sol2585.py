import sys
from math import ceil

input = sys.stdin.readline


def sol2585():
    n, k = map(int, input().split())
    pos = [[0, 0], *[list(map(int, input().split())) for _ in range(n)], [10000, 10000]]

    # 좌표를 기준으로 인접행렬 그래프 생성
    g = [[20001] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                g[i][j] = 0
            else:
                g[i][j] = g[j][i] = ceil(((pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2) ** .5)

    # fuel 만큼의 연료를 담을 수 있는 연료통을 가진채로 출발했을 때
    # 목적지에 도착 가능한지 체크하는 함수 (bfs)
    def takeoff(fuel):
        max_dst = fuel * 10
        visited = [False] * (n + 2)
        q = [0]
        visited[0] = True
        max_cnt = k + 1
        while q and max_cnt:
            nq = []
            for cur in q:
                for nxt in range(n + 2):
                    if cur == nxt:
                        continue
                    if not visited[nxt] and g[cur][nxt] <= max_dst:
                        if nxt == n + 1:
                            return True
                        visited[nxt] = True
                        nq.append(nxt)
            q = nq
            max_cnt -= 1
        return False

    # 연료 가능범위의 최소, 최댓값
    # 중간급유 없이 t까지 직행하는데 필요한 연료통의 크기가 최대치가 됨
    s, e = 1, 1415
    
    # 이분탐색으로 목적지에 도착 가능한 연료통의 크기중 최솟값을 계산
    while s < e:
        mid = (s + e) // 2
        if takeoff(mid):
            e = mid
        else:
            s = mid+1

    return e
