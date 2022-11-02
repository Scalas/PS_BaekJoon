import sys

input = sys.stdin.readline


# 17265 나의 인생에는 수학과 함께
# n * n 격자공간에 체스판 형식으로 행/열의 합이 짝수인 공간에는 숫자가, 홀수인 공간에는 연산자가 적혀있다
# 0, 0 에서 시작하여 n - 1, n - 1 까지 오른쪽 또는 아래로만 이동하며 만난 연산자와 숫자를 계속하여 계산해나갈 때 
# n - 1, n - 1에 도달한 순간 얻을 수 있는 가장 큰 값과 가장 작은 값을 구하는 문제
def sol17265():
    n = int(input())
    board = [input().split() for _ in range(n)]
    max_dp = [[0] * n for _ in range(n)]
    min_dp = [[0] * n for _ in range(n)]
    max_dp[0][0] = min_dp[0][0] = int(board[0][0])
    for i in range(2, n, 2):
        cur1 = int(board[i][0])
        cur2 = int(board[0][i])
        max_dp[i][0] = calc(max_dp[i - 2][0], cur1, [board[i - 1][0]])[0]
        max_dp[0][i] = calc(max_dp[0][i - 2], cur2, [board[0][i - 1]])[0]
        min_dp[i][0] = calc(min_dp[i - 2][0], cur1, [board[i - 1][0]])[0]
        min_dp[0][i] = calc(min_dp[0][i - 2], cur2, [board[0][i - 1]])[0]
    for i in range(1, n):
        for j in range(i % 2, n, 2):
            if j == 0:
                continue
            cur = int(board[i][j])
            max_val = calc(max_dp[i - 1][j - 1], cur, [board[i - 1][j], board[i][j - 1]])[1]
            min_val = calc(min_dp[i - 1][j - 1], cur, [board[i - 1][j], board[i][j - 1]])[0]
            if i >= 2:
                min_val = min(min_val, calc(min_dp[i - 2][j], cur, [board[i - 1][j]])[0])
                max_val = max(max_val, calc(max_dp[i - 2][j], cur, [board[i - 1][j]])[0])
            if j >= 2:
                min_val = min(min_val, calc(min_dp[i][j - 2], cur, [board[i][j - 1]])[0])
                max_val = max(max_val, calc(max_dp[i][j - 2], cur, [board[i][j - 1]])[0])
            max_dp[i][j] = max_val
            min_dp[i][j] = min_val
    return ' '.join(map(str, [max_dp[-1][-1], min_dp[-1][-1]]))


def calc(o1, o2, op_list):
    result = []
    for op in op_list:
        if op == '+':
            result.append(o1 + o2)
        elif op == '-':
            result.append(o1 - o2)
        elif op == '*':
            result.append(o1 * o2)
    result.sort()
    return result
