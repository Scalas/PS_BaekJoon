import sys

input = sys.stdin.readline
mod = 1000000007


# 12849 본대 산책
# 캠퍼스 건물간의 연결관계가 주어지고 연결된 건물간의 이동에 1분이 걸린다고 할 때
# 정보과학관 건물에서 d분간 이동하여 다시 정보과학관으로 돌아오는 경우의 수를 구하는 문제

# dp를 사용하는 방법 - O(N)
def sol12849_1():
    d = int(input())

    # 지도
    g = [
        [1, 2],
        [0, 2, 3],
        [0, 1, 3, 4],
        [1, 2, 4, 5],
        [2, 3, 5, 6],
        [3, 4, 7],
        [4, 7],
        [5, 6]
    ]

    # 각 위치에 도달할 수 있는 경로의 수
    # 0분일 때는 0번(정보과학관)에서 이동하지 않은 1가지 경로뿐
    dp = [0] * 8
    dp[0] = 1

    # d 분동안 1분마다 각 위치에 도달 가능한 경로의 수를 갱신
    for _ in range(d):
        ndp = [0] * 8
        for cur in range(8):
            for nxt in g[cur]:
                ndp[nxt] = (ndp[nxt] + dp[cur]) % mod
        dp = ndp

    # d분이 지난 후 0번(정보과학관)에 도달할 수 있는 경로의 수를 출력
    return dp[0]


# 인접 행렬의 제곱을 활용하는 방법
# 행렬의 빠른 제곱을 사용 - O(logN)
def sol12849_2():
    d = int(input())

    # 그래프의 i번째 노드에서 j번째 노드로 n회의 이동하는 경로의 수는
    # 그래프를 인접행렬로 나타낸 뒤 n제곱 하는 것으로 구할 수 있음

    # 지도를 인접행렬로 표현
    mov = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 0]
    ]

    # 행렬을 d제곱
    after_dmov = mat_sq(mov, d)

    # 정보과학관에서 정보과학관으로 가는 경로의 수 반환
    return after_dmov[0][0] % mod


# 행렬의 곱
def mat_mult(a, b):
    l, m, r = len(a), len(a[0]), len(b[0])
    res = [[0] * r for _ in range(l)]
    for i in range(l):
        for j in range(r):
            for k in range(m):
                res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % mod
    return res


# 행렬의 제곱
def mat_sq(a, n):
    if n == 1:
        return a
    res = mat_sq(a, n//2)
    res = mat_mult(res, res)
    if n % 2:
        res = mat_mult(res, a)
    return res
