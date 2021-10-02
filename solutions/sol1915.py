import sys

input = sys.stdin.readline


# 1915 가장 큰 정사각형
# n x m 배열에서 1로 이루어진 가장 큰 정사각형의 넓이를 구하는 문제
def sol1915():
    # 배열의 크기
    n, m = map(int, input().split())

    # 배열의 상태
    board = [[*map(int, list(input().rstrip())), 0] for _ in range(n)]
    board.append([0]*(m+1))

    # 가장 큰 정사각형의 변의 길이
    answer = 0

    for i in range(n):
        for j in range(m):
            # board[i][j] 가 1일 때, board[i][j] 가 추가되는 것으로 만들어지는 가장 큰 정사각형의 변이 길이는
            # board[i-1][j-1], board[i-1][j], board[i][j-1] 중 가장 작은 값에 1을 더한 것과 같다
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1])+1

                # 가장 큰 정사각형의 변의 길이 갱신
                answer = max(answer, board[i][j])

    # 가장 큰 정사각형의 넓이를 반환
    return answer**2
