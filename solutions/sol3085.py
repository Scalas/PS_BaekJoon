import sys

input = sys.stdin.readline


# 3085 사탕 게임
# 같은 색의 사탕으로 이루어진 가장 긴 연속 부분(가로 혹은 세로)만큼의 사탕을 가져갈 수 있으며
# 보드 위의 두 사탕의 위치를 한번 맞바꿀 수 있다고 할때 가져갈 수 있는 사탕의 최대갯수를 구하는 문제
def sol3085():
    n = int(input())
    board = [list(input().rstrip()) for _ in range(n)]

    # 해당 위치를 기준으로 같은 색의 사탕으로 이루어진 가장 긴 연속부분의 길이를 구하는 함수
    def len_check(board, n, r, c):
        f = board[r][c]
        # 세로
        rc = 1
        for i in range(r - 1, -1, -1):
            if board[i][c] == f:
                rc += 1
            else:
                break
        for i in range(r + 1, n):
            if board[i][c] == f:
                rc += 1
            else:
                break

        # 가로
        cc = 1
        for i in range(c - 1, -1, -1):
            if board[r][i] == f:
                cc += 1
            else:
                break
        for i in range(c + 1, n):
            if board[r][i] == f:
                cc += 1
            else:
                break
        return max(rc, cc)

    answer = 0
    # 보드의 모든 칸에 대해
    for r in range(n):
        for c in range(n):
            # 오른쪽 칸, 아래쪽 칸과 사탕을 교환하고 가장 긴 연속부분의 길이를 체크하여 answer 값을 갱신한다
            # 위쪽, 왼쪽을 조사하지 않는 것은 이미 위나 왼쪽의 칸에서 현재 칸과의 교환을 수행했기 때문
            for nr, nc in [(r + 1, c), (r, c + 1)]:
                if nr < n and nc < n:
                    board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
                    answer = max(answer, len_check(board, n, r, c))
                    answer = max(answer, len_check(board, n, nr, nc))
                    board[r][c], board[nr][nc] = board[nr][nc], board[r][c]

    # 가져갈 수 있는 사탕의 최대갯수 반환
    return answer
