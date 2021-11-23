import sys

input = sys.stdin.readline


# 1051 숫자 정사각형
# 한자리 숫자가 쓰여진 격자지도에서 네 꼭지점의 수가 모두 같은 정사각형의 최대 크기를 구하는 문제
def sol1051():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    for size in range(max(n, m), 1, -1):
        for i in range(n-size+1):
            for j in range(m-size+1):
                r, c = i+size-1, j+size-1
                if board[i][j] == board[r][j] == board[i][c] == board[r][c]:
                    return size ** 2
    return 1


