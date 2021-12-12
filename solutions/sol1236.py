import sys

input = sys.stdin.readline


# 1236 성 지키기
# n * m 공간의 초기상태가 주어졌을 때 모든 행과 열에 최소 하나의 경비원이 있도록 하기 위해
# 추가로 필요한 경비원의 수를 구하는 문제
def sol1236():
    n, m = map(int, input().split())
    # 각 행과 열의 경비원 수를 파악
    row, col = [0] * n, [0] * m
    for i in range(n):
        line = input().rstrip()
        for j in range(m):
            if line[j] == 'X':
                row[i] += 1
                col[j] += 1

    # 경비원이 없는 행과 열의 수를 각각 구하여 그중 최댓값을 반환
    rc, cc = 0, 0
    for r in row:
        if not r:
            rc += 1
    for c in col:
        if not c:
            cc += 1

    return max(rc, cc)
