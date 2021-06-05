import sys

input = sys.stdin.readline


# 2447 별찍기
# 재귀호출을 통해 별 패턴을 그리는 문제

# 첫 번째 시도
# 단순히 n*n 크기의 *로 채워진 배열을 만든 후
# 재귀적으로 공백을 만들어 패턴을 그림
# 풀리긴 하지만 매 호출마다 (n//2)^2 의 반복문을 돌려야해서 속도가 느림
def sol2447():
    n = int(input())
    board = [['*'] * n for _ in range(n)]
    draw(board, 0, 0, n)
    print('\n'.join(map(''.join, board)))


def draw(board, r, c, n):
    if n == 3:
        board[r + 1][c + 1] = ' '
    else:
        m = n // 3
        for i in range(3):
            for j in range(3):
                if not i == j == 1:
                    draw(board, r + i * m, c + j * m, m)
        for i in range(m):
            for j in range(m):
                board[r+m+i][c+m+j] = ' '


# 다른 코드를 본뒤 두 번째 시도
# zip 을 활용한 풀이
def sol2447_2():
    n = int(input())
    print('\n'.join(draw_2(n)))


def draw_2(n):
    if n == 3:
        return ['***', '* *', '***']
    m = n//3

    # 각 칸을 구성할 작은 사각형
    sub = draw_2(m)

    # 작은 사각형 3개로 이루어진 위, 아랫부분
    term = list(map(''.join, zip(sub, sub, sub)))

    # 양쪽에 작은사각형, 가운데 공백으로 이루어진 가운데부분
    mid = list(map(''.join, zip(sub, [' '*m]*m, sub)))

    # 하나의 리스트로 합쳐서 반환
    return term+mid+term
