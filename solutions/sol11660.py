import sys

input = sys.stdin.readline


# 11660 구간 합 구하기 5
# 2차원 누적합의 성질을 활용하는 문제
def sol11660():
    # 표의 크기, 질의의 갯수
    n, m = map(int, input().split())

    # 표의 상태
    board = [[0, *map(int, input().split())] if i else [0]*(n+1) for i in range(n+1)]

    # 표의 2차원 누적합을 구한다
    for i in range(1, n):
        for j in range(1, n+1):
            board[i + 1][j] += board[i][j]
            board[i][j] += board[i][j - 1]
    for i in range(1, n+1):
        board[n][i] += board[n][i - 1]

    # 질의에 대한 정답 리스트
    answer = []
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        answer.append(board[x2][y2] - board[x1 - 1][y2] - board[x2][y1 - 1] + board[x1 - 1][y1 - 1])

    # 출력형식에 맞춰 정답 리스트 반환
    return '\n'.join(map(str, answer))
