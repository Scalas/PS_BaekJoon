import sys

input = sys.stdin.readline


# 10709 기상캐스터
# h * w 공간에 구름의 위치가 주어지고 구름은 매 분마다 동쪽으로 한칸씩 이동할 때
# 각 지역에 몇분 후에 구름이 오는지 구하는 문제
def sol10709():
    h, w = map(int, input().split())
    board = [[-1] * w for _ in range(h)]
    for i in range(h):
        line = list(input().rstrip())
        for j in range(w):
            if line[j] == 'c':
                board[i][j] = 0

    for i in range(h):
        for j in range(w):
            if j > 0 and board[i][j] < 0 and board[i][j-1] >= 0:
                board[i][j] = board[i][j-1] + 1
    return '\n'.join([' '.join(map(str, line)) for line in board])
