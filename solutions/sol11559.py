import sys

input = sys.stdin.readline


# 11559 Puyo Puyo
# 뿌요뿌요 필드가 주어졌을 때 일어나는 연쇄의 수를 구하는 문제
def sol11559():
    # 게임 필드
    board = [list(input().rstrip()) for _ in range(12)]

    # 연쇄 수
    answer = 0

    while True:
        # 터진 뿌요 묶음의 수
        cnt = 0

        # bfs로 4개이상 뭉친 뿌요를 터트리고 터진 묶음의 수를 센다
        visited = [[False] * 6 for _ in range(12)]
        for i in range(12):
            for j in range(6):
                if board[i][j] != '.':
                    cnt += bfs(board, visited, i, j)

        # 뿌요가 하나도 터지지 않으면 반복종료
        if not cnt:
            break

        # 뿌요가 터졌으면 연쇄수 1 증가
        answer += 1

        # 뿌요의 이동(빈자리채우기)
        # 마지막 행의 위쪽 행부터 이동시작
        for i in range(10, -1, -1):
            for j in range(6):
                curi = i
                # 마지막 행에 도달하거나 아래쪽이 빈칸(.)이 아닐 때 까지 내려간다
                while curi < 11 and board[curi+1][j] == '.':
                    board[curi+1][j], board[curi][j] = board[curi][j], '.'
                    curi += 1

    return answer


# bfs 함수
# 4개이상의 같은색 뿌요뭉치가 있으면 터트린다(.으로 변경)
# 터지지 않더라도 visited 는 갱신한다
# 뿌요뭉치가 터졌다면 1, 그렇지 않다면 0을 반환한다
def bfs(board, visited, r, c):
    q = [(r, c)]
    color = board[r][c]
    chained = []
    while q:
        nq = []
        for r, c in q:
            if r-1 >= 0 and board[r-1][c] == color and not visited[r-1][c]:
                visited[r-1][c] = True
                chained.append((r-1, c))
                nq.append((r-1, c))
            if r+1 < 12 and board[r+1][c] == color and not visited[r+1][c]:
                visited[r+1][c] = True
                chained.append((r+1, c))
                nq.append((r+1, c))
            if c-1 >= 0 and board[r][c-1] == color and not visited[r][c-1]:
                visited[r][c-1] = True
                chained.append((r, c-1))
                nq.append((r, c-1))
            if c+1 < 6 and board[r][c+1] == color and not visited[r][c+1]:
                visited[r][c+1] = True
                chained.append((r, c+1))
                nq.append((r, c+1))
        q = nq

    if len(chained) >= 4:
        for r, c in chained:
            board[r][c] = '.'
        return 1
    return 0


if __name__ == '__main__':
    print(sol11559())
