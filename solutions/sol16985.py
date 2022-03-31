import sys
from itertools import permutations, product

input = sys.stdin.readline
INF = 126


# 16985 Maaaaaaaaaze
# 5 * 5 * 5 3차원 미궁의 각 층을 회전 가능할 때
# 미궁의 한 모서리에서 면을 공유하지 않는 반대편 모서리로 이동하는 최단거리를 구하는 문제
def sol16985():

    def bfs(cube, sx, sy, sz, ex, ey, ez):
        visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
        q = [(sx, sy, sz)]
        visited[sx][sy][sz] = True
        cnt = -1
        while q:
            cnt += 1
            if answer == cnt:
                break
            nq = []
            for x, y, z in q:
                if x == ex and y == ey and z == ez:
                    return cnt
                if x > 0:
                    if not visited[x-1][y][z] and cube[x-1][y][z]:
                        visited[x-1][y][z] = True
                        nq.append((x-1, y, z))

                if x < 4:
                    if not visited[x+1][y][z] and cube[x+1][y][z]:
                        visited[x+1][y][z] = True
                        nq.append((x+1, y, z))

                if y > 0:
                    if not visited[x][y-1][z] and cube[x][y-1][z]:
                        visited[x][y-1][z] = True
                        nq.append((x, y-1, z))

                if y < 4:
                    if not visited[x][y+1][z] and cube[x][y+1][z]:
                        visited[x][y+1][z] = True
                        nq.append((x, y+1, z))

                if z > 0:
                    if not visited[x][y][z-1] and cube[x][y][z-1]:
                        visited[x][y][z-1] = True
                        nq.append((x, y, z-1))

                if z < 4:
                    if not visited[x][y][z+1] and cube[x][y][z+1]:
                        visited[x][y][z+1] = True
                        nq.append((x, y, z+1))
            q = nq

        return INF

    # 각 판의 회전상태
    plates = [[] for _ in range(5)]
    for i in range(5):
        plate = [tuple(map(int, input().split())) for _ in range(5)]
        plates[i].append(plate)
        plate = rotate(plate)
        plates[i].append(plate)
        plate = rotate(plate)
        plates[i].append(plate)
        plate = rotate(plate)
        plates[i].append(plate)

    # 판의 순서
    layers = [0, 1, 2, 3, 4]
    rotations = [0, 1, 2, 3]

    # 가능한 모든 미궁의 형태를 체크하여 최단거리탐색
    answer = INF
    for order in permutations(layers, 5):
        for rotation in product(rotations, repeat=5):
            cube = [plates[order[i]][rotation[i]] for i in range(5)]

            if cube[0][0][0] and cube[4][4][4]:
                answer = min(answer, bfs(cube, 0, 0, 0, 4, 4, 4))

            if answer == 12:
                break

    return answer if answer != INF else -1


# 판을 시계방향으로 한번 회전
def rotate(board):
    return [line[::-1] for line in zip(*board)]
