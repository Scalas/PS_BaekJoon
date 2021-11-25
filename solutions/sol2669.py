import sys

input = sys.stdin.readline


# 2669 직사각형 네개의 합집합
# 네 개의 직사각형의 좌 하단, 우 상단의 꼭짓점 좌표가 주어졌을 때
# 직사각형들이 차지하는 총 넓이를 구하는 문제
# 2차원 누적합으로 해결
def sol2669():
    board = [[0] * 101 for _ in range(101)]
    for _ in range(4):
        v, w, x, y = map(int, input().split())
        board[v][w] += 1
        board[x][y] += 1
        board[v][y] -= 1
        board[x][w] -= 1

    answer = 0
    for i in range(1, 100):
        for j in range(1, 101):
            board[i+1][j] += board[i][j]
            board[i][j] += board[i][j-1]
            if board[i][j]:
                answer += 1
    return answer

