from sys import stdin


# 1018 체스판 다시 칠하기
# 주어진 판을 8*8크기로 잘라낸 후 색을 칠해 체스판을 만들 때
# 칠해야할 수 중 가장 적은 값을 찾는 문제
def sol1018():
    n, m = map(int, stdin.readline().split())
    board = [stdin.readline().rstrip() for _ in range(n)]
    answer = 64
    # 체스판의 시작점이 될 수 있는 모든 점에 대해 탐색
    for i in range(n - 7):
        for j in range(m - 7):
            # 시작점에서부터 체스판의 크기만큼 순회하며 시작점이 흰색일때와 검은색일때 칠해야할 수를 카운트
            res = [0, 0]
            for r in range(i, i+8):
                for c in range(j, j+8):
                    check = (r + c) % 2
                    if board[r][c] == 'W':
                        res[check] += 1
                    else:
                        res[1 - check] += 1

            # 최솟값 갱신
            answer = min(answer, min(res))
    print(answer)
