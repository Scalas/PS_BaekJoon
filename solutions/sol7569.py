import sys


# 7569 토마토
# 7568 토마토 문제의 3차원버전
def sol7569(m, n, h, tomato):
    q = []
    cnt = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k] == 1:
                    q.append((i, j, k))
                elif tomato[i][j][k] == 0:
                    cnt += 1

    if cnt == 0:
        return 0

    answer = 0
    while q and cnt:
        nq = []
        for z, r, c in q:
            if z > 0 and not tomato[z - 1][r][c]:
                tomato[z - 1][r][c] = 1
                cnt -= 1
                nq.append((z - 1, r, c))
            if z < h - 1 and not tomato[z + 1][r][c]:
                tomato[z + 1][r][c] = 1
                cnt -= 1
                nq.append((z + 1, r, c))
            if r > 0 and not tomato[z][r - 1][c]:
                tomato[z][r - 1][c] = 1
                cnt -= 1
                nq.append((z, r - 1, c))
            if r < n - 1 and not tomato[z][r + 1][c]:
                tomato[z][r + 1][c] = 1
                cnt -= 1
                nq.append((z, r + 1, c))
            if c > 0 and not tomato[z][r][c - 1]:
                tomato[z][r][c - 1] = 1
                cnt -= 1
                nq.append((z, r, c - 1))
            if c < m - 1 and not tomato[z][r][c + 1]:
                tomato[z][r][c + 1] = 1
                cnt -= 1
                nq.append((z, r, c + 1))
        answer += 1
        q = nq
    return -1 if cnt else answer


input = sys.stdin.readline
m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

if __name__ == '__main__':
    print(sol7569(m, n, h, tomato))
