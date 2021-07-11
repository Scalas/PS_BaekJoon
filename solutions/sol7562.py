import sys

input = sys.stdin.readline
direction = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, -2), (-1, -2), (1, 2), (-1, 2)]


# 7562 나이트의 이동
# 나이트가 현재좌표에서 특정 좌표로 이동하는데 필요한 최소 이동횟수를 구하는문제
# bfs로 간단히 해결 가능
def sol7562():
    answer = []
    for t in range(int(input())):
        n = int(input())
        kx, ky = map(int, input().split())
        tx, ty = map(int, input().split())

        visit = [[False] * n for _ in range(n)]
        q = [(kx, ky)]
        visit[kx][ky] = True
        turn = 0
        check = False
        while q:
            nq = []
            for x, y in q:
                if x == tx and y == ty:
                    answer.append(str(turn))
                    check = True
                    break
                for d in direction:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                        visit[nx][ny] = True
                        nq.append((nx, ny))
            if check:
                break
            q = nq
            turn += 1

    print('\n'.join(answer))
