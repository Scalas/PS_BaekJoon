import sys

input = sys.stdin.readline


# 2580 스도쿠
# 빈칸이 0으로 주어진 9*9 스도쿠 문제를 풀어서 결과를 출력하는 문제
# 빈칸마다 1에서 9까지의 수 중에 같은 3*3 정사각형 내에 들어가지 않고 가로, 세로에 같은 숫자가 없는 수를 넣어볼 수 있다
# 그 확인을 매번 반복문으로 한다면 가로, 세로, 정사각형 내에서 각각 8씩 24번의 확인이 필요
# row, col grid 별 해당 숫자가 존재하는지 체크하는 리스트를 두어 그 시간을 조금이라도 줄인다
# 빈칸의 갯수가 DFS 의 깊이가 되고 소요시간을 좌우한다.
# 이 문제에서는 빈칸의 갯수가 일정 이상으로 주어지지 않아 Python3으로도 통과할 수 있었다.


# 다른 풀이를 보니 DFS 를 사용하지 않고 빈칸이 많아도 순식간에 답을 구하는 훨씬 빠른 풀이도 있지만
# 너무 복잡하고 정해진 시간내에 생각해내고 구현할 수 있을것으로 보이지 않아서 여기서는 다루지 않는다
def sol2580():
    board = []
    spaces = []
    rowcheck = [[False] * 9 for _ in range(9)]
    colcheck = [[False] * 9 for _ in range(9)]
    gridcheck = [[False] * 9 for _ in range(9)]
    for r in range(9):
        line = list(map(int, input().split()))
        for c in range(9):
            num = line[c]
            if (num == 0):
                spaces.append((r, c))
            else:
                rowcheck[r][num - 1] = True
                colcheck[c][num - 1] = True
                gridcheck[(r // 3) * 3 + c // 3][num - 1] = True

        board.append(line)

    dfs(board, rowcheck, colcheck, gridcheck, spaces, 0)


def dfs(board, rowcheck, colcheck, gridcheck, spaces, idx):
    if (idx == len(spaces)):
        print('\n'.join([' '.join(map(str, line)) for line in board]))
        sys.exit(0)
    r, c = spaces[idx]
    g = (r // 3) * 3 + c // 3
    for num in range(1, 10):
        if not (rowcheck[r][num - 1] or colcheck[c][num - 1] or gridcheck[g][num - 1]):
            rowcheck[r][num - 1] = True
            colcheck[c][num - 1] = True
            gridcheck[g][num - 1] = True
            board[r][c] = num
            dfs(board, rowcheck, colcheck, gridcheck, spaces, idx + 1)
            rowcheck[r][num - 1] = False
            colcheck[c][num - 1] = False
            gridcheck[g][num - 1] = False
            board[r][c] = 0
