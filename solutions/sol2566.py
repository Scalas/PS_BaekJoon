import sys

input = sys.stdin.readline


# 2566 최댓값
# 9 * 9 격자판에서 최댓값의 행, 열 번호를 출력하는 문제
def sol2566():
    maxi, maxj, maxv = 0, 0, 0
    for i in range(9):
        line = list(map(int, input().split()))
        for j in range(9):
            if maxv < line[j]:
                maxi, maxj, maxv = i, j, line[j]
    return '\n'.join([str(maxv), ' '.join([str(maxi+1), str(maxj+1)])])
