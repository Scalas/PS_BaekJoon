import sys

input = sys.stdin.readline


# 9663 N-Queen
# 8-Queens 문제의 파생
# n*n 보드위에 n개의 퀸을 서로 공격할수 없게 놓는 문제
# 완전탐색을 통해 풀 수 있지만 시간을 줄이기 위해 많은 최적화가 필요

# 가장 기본적인 최적화는 promising(유망)함수의 구현
# 더이상 탐색하는 의미가 없을 경우 탐색을 그만두도록 해야 쓸데없는 시간 소모를 줄일 수 있다
# 하지만 매번 겹치는 퀸이 있는지 검사하는 것은 그것만으로 O(N^2)이므로 여전히 시간 소모가 심하다


# 첫 번째 시도
# 각 행에 퀸은 하나씩만 존재하기 때문에 모든 칸을 검사할 필요 없이 그 행에서 놓으려는 퀸과 겹칠 가능성이 있는 칸만 검사
# 열이 같은경우, 좌대각으로 겹치는 경우, 우대각으로 겹치는 경우 총 세 가지 케이스가 있기 때문에
# 검사해야할 칸 수가 N^2 에서 3*N으로 줄어든다
# O(N^2)의 유망 함수에 비하면 훨씬 나은 성능이지만 파이썬에서는 여전히 시간초과 발생
def sol9663():
    n = int(input())
    board = [[0] * n for _ in range(n)]
    answer = dfs(board, n, 0)
    print(answer)


def dfs(board, n, cnt):
    if (cnt == n):
        return 1
    res = 0
    for c in range(n):
        if not promising(board, cnt, c):
            continue
        board[cnt][c] = 1
        res += dfs(board, n, cnt + 1)
        board[cnt][c] = 0
    return res


def promising(board, r, c):
    l = len(board)
    for i in range(r):
        if(board[i][c]==1):
            return False
        elif(0<=r+c-i<l and board[i][r+c-i]==1):
            return False
        elif(0<=i-r+c<l and board[i][i-r+c]==1):
            return False
    return True


# 두 번째 시도
# 퀸을 놓을 수 없는 것은 이전 행에 열이 같은 퀸이 하나라도 존재하거나
# row, col 값을 더하거나 뺀 값이 같은 퀸이 하나라도 존재하는 경우이다
# 그러므로 퀸을 놓을 때마다 row+col, row-col, col 의 값에 카운트를 해주면
# 놓으려는 자리의 row, col 값에 대응하는 저 세 값중 하나라도 1 이상일 경우 유망하지 않다고 판단할 수 있다
# 유망함의 판단을 O(1)로 끝낼 수 있어 첫 번째 풀이보다 훨씬 나은 성능을 보인다.
# 하지만 여전히 Python3 기준으로는 시간초과가 발생.  PyPy3에서만 간신히 통과할 수 있었다.
# 완전탐색 문제는 대체로 속도가 느린 Python 에는 불리한 문제이기에 이를 보조하기 위해 C++ 등의 속도가 빠른 언어를
# 익혀둘 필요가 있다.
def sol9663_2():
    n = int(input())
    rdiag = [0]*(2*n-1)
    ldiag = [0]*(2*n-1)
    col = [0]*n
    answer = dfs(rdiag, ldiag, col, n, 0)
    print(answer)


def dfs(rdiag, ldiag, col, n, cnt):
    if (cnt == n):
        return 1
    res = 0
    for c in range(n):
        if rdiag[cnt+c] > 0 or ldiag[cnt-c+n-1] > 0 or col[c] > 0:
            continue
        rdiag[cnt+c] += 1
        ldiag[cnt-c + n-1] += 1
        col[c] += 1
        res += dfs(rdiag, ldiag, col, n, cnt + 1)
        rdiag[cnt+c] -= 1
        ldiag[cnt-c + n-1] -= 1
        col[c] -= 1
    return res
