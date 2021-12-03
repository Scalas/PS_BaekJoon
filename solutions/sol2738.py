import sys

input = sys.stdin.readline


# 2738 행렬 덧셈
# 주어진 n * m 행렬 두개를 더한 행렬을 구하는 문제
def sol2738():
    n, m = map(int, input().split())
    mat = [[0] * m for _ in range(n)]
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            mat[i][j] += line[j]
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            mat[i][j] += line[j]
    return '\n'.join([' '.join(map(str, mat[i])) for i in range(n)])

