import sys

input = sys.stdin.readline


# 25682 체스판 다시 칠하기 2
# n * m 크기의 보드의 각 칸이 컴은색 또는 하얀색으로 칠해져있고
# 그중 k * k 크기의 보드를 잘라내 체스판모양으로 칠할 때
# 칠해야할 칸 수의 최솟값을 구하는 문제
def sol25682():
    n, m, k = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]

    # 첫 칸을 검은색으로 할 경우와 흰색으로 할 경우로 나누어 규칙에 어긋나는 칸의 수치를 1로 하면
    # 범위 내의 2차원 누적합의 값이 그 범위를 체스판 모양으로 칠할 때 칠해야할 칸의 갯수를 의미하게된다.
    # 모든 k * k 크기의 보드를 자르는 경우에 대해 이 값을 구하여 그중 최솟값을 구한다.
    black_acc_table = [[0] * (m + 1) for _ in range(n + 1)]
    white_acc_table = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'B':
                if (i + j) % 2:
                    black_acc_table[i][j] = 1
                else:
                    white_acc_table[i][j] = 1
            else:
                if (i + j) % 2:
                    white_acc_table[i][j] = 1
                else:
                    black_acc_table[i][j] = 1
    for i in range(n - 1):
        for j in range(m):
            black_acc_table[i + 1][j] += black_acc_table[i][j]
            black_acc_table[i][j] += black_acc_table[i][j - 1]
            white_acc_table[i + 1][j] += white_acc_table[i][j]
            white_acc_table[i][j] += white_acc_table[i][j - 1]
    for i in range(m):
        black_acc_table[n - 1][i] += black_acc_table[n - 1][i - 1]
        white_acc_table[n - 1][i] += white_acc_table[n - 1][i - 1]

    answer = n * m
    for si in range(n - k + 1):
        for sj in range(m - k + 1):
            ei, ej = si + k - 1, sj + k - 1
            cur_min = min(
                black_acc_table[ei][ej] - black_acc_table[ei][sj - 1] - black_acc_table[si - 1][ej] + black_acc_table[si - 1][sj - 1],
                white_acc_table[ei][ej] - white_acc_table[ei][sj - 1] - white_acc_table[si - 1][ej] + white_acc_table[si - 1][sj - 1]
            )

            answer = min(answer, cur_min)
    return answer
