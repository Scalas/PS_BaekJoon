import sys

input = sys.stdin.readline


def sol1451():
    n, m = map(int, input().split())
    square = [[0] * (m + 1) for _ in range(n + 1)]

    # 직사각형에 적힌 수들의 2차원 누적합을 계산
    for i in range(n):
        line = list(map(int, list(input().rstrip())))
        for j in range(m):
            square[i][j] = line[j]

    for i in range(n):
        for j in range(m):
            if i < n - 1:
                square[i + 1][j] += square[i][j]
            if j > 0:
                square[i][j] += square[i][j - 1]

    # i, j 를 경계가 되는 지점으로 했을 때 가능한 모든 케이스를 계산
    answer = 0
    total = square[n - 1][m - 1]
    for i in range(n):
        for j in range(m):
            part1 = square[i][j]
            part2 = (square[n - 1][j] - square[i][j])
            part3 = total - part1 - part2
            answer = max(answer, part1 * part2 * part3)

            part1 = square[i][j]
            part2 = (square[i][m - 1] - square[i][j])
            part3 = total - part1 - part2
            answer = max(answer, part1 * part2 * part3)

            part1 = square[i][m - 1] - square[i][j - 1]
            part2 = square[i][j - 1]
            part3 = total - part1 - part2
            answer = max(answer, part1 * part2 * part3)

            part1 = square[i][m - 1] - square[i][j - 1]
            part2 = square[n - 1][j - 1]
            part3 = total - part1 - part2
            answer = max(answer, part1 * part2 * part3)

            part1 = square[i - 1][m - 1]
            part2 = square[n - 1][j - 1] - square[i - 1][j - 1]
            part3 = total - part1 - part2
            answer = max(answer, part1 * part2 * part3)

            part1 = square[n - 1][j - 1]
            part2 = square[i - 1][m - 1] - square[i - 1][j - 1]
            part3 = total - part1 - part2
            answer = max(answer, part1 * part2 * part3)

            part1 = square[i - 1][m - 1]
            part2 = square[n - 1][j] - square[i - 1][j]
            part3 = total - part1 - part2
            answer = max(answer, part1 * part2 * part3)

            part1 = square[n - 1][m - 1] - square[n - 1][j]
            part2 = square[i - 1][j]
            part3 = total - part1 - part2
            answer = max(answer, part1 * part2 * part3)

    # 직사각형을 수직, 혹은 수평선으로만 자르는 경우
    for i in range(m - 2):
        for j in range(i + 1, m - 1):
            part1 = square[n - 1][i]
            part2 = (square[n - 1][j] - square[n - 1][i])
            part3 = total - part1 - part2
            answer = max(answer, part1 * part2 * part3)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            part1 = square[i][m - 1]
            part2 = (square[j][m - 1] - square[i][m - 1])
            part3 = total - part1 - part2
            answer = max(answer, part1 * part2 * part3)

    return answer
