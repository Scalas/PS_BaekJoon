import sys

input = sys.stdin.readline


# 14925 목장 건설하기
# n, m 크기의 공간의 각 칸마다 들판(0), 나무(1), 돌(2)이 위치하고있을 때
# 들판으로만 이루어진 정사각형 중 가장 큰 것의 한 변의 길이를 구하는 문제
def sol14925():
    n, m = map(int, input().split())

    # 공간의 상태
    land = [list(map(int, input().split())) for _ in range(n)]

    # (i, j) 에서 끝나는 정사각형의 최대 크기
    area = [[-1] * m for _ in range(n)]

    # (i, j) 에서 끝나는 연속된 들판의 너비, 높이
    height = [[0] * m for _ in range(n)]
    width = [[0] * m for _ in range(n)]

    answer = 0

    # area[i][j] 계산
    # 1. (i, j) 가 0이 아닐 경우 0
    # 2. (i, j) 가 0일 경우
    # 2-1. (i - 1, j - 1)가 들판이 아닐 경우 1
    # 2-2. (i - 1, j - 1)가 들판이라면 area[i - 1][j - 1] + 1, width[i][j], height[i][j] 중 최솟값
    for i in range(n):
        area[i][0] = height[i][0] = width[i][0] = 0 if land[i][0] else 1
        if area[i][0]:
            answer = 1

    for i in range(m):
        area[0][i] = width[0][i] = height[0][i] = 0 if land[0][i] else 1
        if area[0][i]:
            answer = 1

    for i in range(1, n):
        for j in range(1, m):
            if land[i][j]:
                height[i][j] = width[i][j] = area[i][j] = 0
                continue

            height[i][j] = height[i - 1][j] + 1
            width[i][j] = width[i][j - 1] + 1

            area[i][j] = min(height[i][j], width[i][j], area[i - 1][j - 1] + 1)
            answer = max(answer, area[i][j])

    return answer
