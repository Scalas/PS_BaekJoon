from sys import stdin


# 9184 신나는 함수 실행
# 재귀함수를 동적계획법으로 개선하는 문제
def sol9184():
    w = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                if i < j < k:
                    w[i][j][k] = w[i][j][k - 1] + w[i][j - 1][k - 1] - w[i][j - 1][k]
                else:
                    w[i][j][k] = w[i - 1][j][k] + w[i - 1][j - 1][k] + w[i - 1][j][k - 1] - w[i - 1][j - 1][k - 1]
    answer = []
    for i in stdin:
        a, b, c = map(int, i.split())
        if a == b == c == -1:
            break
        if a <= 0 or b <= 0 or c <= 0:
            answer.append(f'w({a}, {b}, {c}) = 1')
        elif a > 20 or b > 20 or c > 20:
            answer.append(f'w({a}, {b}, {c}) = {w[20][20][20]}')
        else:
            answer.append(f'w({a}, {b}, {c}) = {w[a][b][c]}')
    print('\n'.join(answer))
