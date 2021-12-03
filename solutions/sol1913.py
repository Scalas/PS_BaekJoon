import sys

input = sys.stdin.read


# 1913 달팽이
# 홀수 n과 n^2 이하의 자연수 m이 주어졌을 때
# 1부터 n^2 까지의 자연수를 달팽이모양으로 n * n 배열에 나타내고
# m 값의 배열에서의 좌표를 구하는 문제
def sol1913():
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]

    # 시작점 - 배열의 중앙
    r = c = n // 2
    board[r][c] = 1

    # m값의 좌표 - 초기값은 중앙으로 설정
    board.append([r+1, c+1])

    # 배열에 넣을 숫자 (1 ~ n ^ 2)
    num = 2

    # 반복 1회당 달팽이 1바퀴씩 두르기
    # m을 찾을 시 좌표 갱신
    for i in range(n // 2):
        # 위, 오른쪽의 길이 = 2 * i + 1
        # 아래, 왼쪽의 길이 = 2 * i + 2
        dst1, dst2 = 2 * i + 1, 2 * i + 2

        # 위로 이동
        for _ in range(dst1):
            r, c = r-1, c
            board[r][c] = num
            if num == m:
                board[-1] = r+1, c+1
            num += 1

        # 오른쪽으로 이동
        for _ in range(dst1):
            r, c = r, c+1
            board[r][c] = num
            if num == m:
                board[-1] = r+1, c+1
            num += 1

        # 아래로 이동
        for _ in range(dst2):
            r, c = r+1, c
            board[r][c] = num
            if num == m:
                board[-1] = r+1, c+1
            num += 1

        # 왼쪽으로 이동
        for _ in range(dst2):
            r, c = r, c-1
            board[r][c] = num
            if num == m:
                board[-1] = r+1, c+1
            num += 1

    # 마지막으로 위로 올라가며 남은 칸을 메꿈
    for _ in range(n-1):
        r, c = r-1, c
        board[r][c] = num
        if num == m:
            board[-1] = r+1, c+1
        num += 1

    return '\n'.join([' '.join(map(str, board[i])) for i in range(n+1)])
