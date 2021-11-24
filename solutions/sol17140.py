import sys
from collections import defaultdict

input = sys.stdin.readline


# 17140 이차원 배열과 연산
# 3 * 3 행렬에서 1초마다 행의 갯수가 열의 갯수 이상이라면 R, 그렇지 않다면 C 연산을 수행하여
# 몇 초째에 arr[r][c] 가 k가 되는지 구하는 문제. (100초가 넘어가면 -1)
def sol17140():
    r, c, k = map(int, input().split())
    n, m = 3, 3
    arr = [[0] * 100 for _ in range(100)]
    for i in range(3):
        line = [*map(int, input().split())]
        for j in range(3):
            arr[i][j] = line[j]

    time = 0
    while arr[r-1][c-1] != k and time < 100:
        # R 연산
        if n >= m:
            for i in range(n):
                m = max(m, rsort(arr, i, m))

        # C 연산
        else:
            for i in range(m):
                n = csort(arr, i, n)

        time += 1
    return time if time < 100 else -1


def rsort(arr, r, size):
    d = defaultdict(int)
    for i in range(size):
        if arr[r][i]:
            d[arr[r][i]] += 1
    res = []
    for num in sorted(d.keys(), key = lambda x: (d[x], x))[:min(len(d), 50)]:
        res.append(num)
        res.append(d[num])

    size = max(len(res), size)
    for i in range(size):
        if i < len(res):
            arr[r][i] = res[i]
        else:
            arr[r][i] = 0
    return size


def csort(arr, c, size):
    d = defaultdict(int)
    for i in range(size):
        if arr[i][c]:
            d[arr[i][c]] += 1
    res = []
    for num in sorted(d.keys(), key = lambda x: (d[x], x))[:min(len(d), 50)]:
        res.append(num)
        res.append(d[num])

    size = max(len(res), size)
    for i in range(size):
        if i < len(res):
            arr[i][c] = res[i]
        else:
            arr[i][c] = 0
    return size
