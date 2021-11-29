import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = n * m
total = sum([sum(board[i]) for i in range(n)])


# 17822 원판 돌리기
# i번째 줄의 j번쨰 수가 중심으로부터 i번째 원판의 12시방향부터 시작하여 시계방향으로 j번 째 수라고 할때
# x : 원판의 번호 / d : 회전방향 (0 시계 / 1 반시계) / k : 회전 칸수
# 위 세 개의 정보를 담은 t개의 명령에 대해 x의 배수번째 원판을 모두 회전하고
# 좌, 우, 이전원판, 다음 원판의 인접하며 같은 값을 가진 수를 모두 삭제하는 연산을 수행한다.
# 연산이 모두 끝났을 때 원판에 남아있는 수의 합을 구하는 문제
def sol17822():
    global total, cnt

    for _ in range(t):
        x, d, k = map(int, input().split())
        # 원판 회전
        for i in range(x, n+1, x):
            i -= 1
            if not d:
                board[i] = board[i][m-k:] + board[i][:m-k]
            else:
                board[i] = board[i][k:] + board[i][:k]

        # 인접한 수 탐색
        if not cnt:
            return total

        removed = 0
        for i in range(n):
            for j in range(m):
                if board[i][j]:
                    removed += dfs(i, j, 0)

        # 어떤 수도 삭제되지 않은 경우
        if not removed:
            avg = total / cnt
            for i in range(n):
                for j in range(m):
                    if not board[i][j]:
                        continue
                    if board[i][j] > avg:
                        board[i][j] -= 1
                        total -= 1
                    elif board[i][j] < avg:
                        board[i][j] += 1
                        total += 1

    return total


def dfs(i, j, removed):
    global total, cnt

    key = board[i][j]

    # 왼쪽
    left = j-1 if j else m-1
    if board[i][left] == key:
        board[i][j] = 0
        removed += dfs(i, left, 1)

    # 오른쪽
    right = j+1 if j < m-1 else 0
    if board[i][right] == key:
        board[i][j] = 0
        removed += dfs(i, right, 1)

    # 이전 원판
    if i > 0 and board[i-1][j] == key:
        board[i][j] = 0
        removed += dfs(i-1, j, 1)

    # 다음 원판
    if i < n-1 and board[i+1][j] == key:
        board[i][j] = 0
        removed += dfs(i+1, j, 1)

    # 현재 위치
    if removed:
        total -= key
        cnt -= 1
        board[i][j] = 0

    return 1 if removed else 0
