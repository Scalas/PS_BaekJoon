import sys
from math import ceil

input = sys.stdin.readline
INF = 10 ** 9


# 4902 삼각형의 값
# 길이 1의 정삼각형을 이어붙여 만든 최대 400행의 정삼각형이 주어지고
# 각 길이 1의 정삼각형마다 절댓값 1000 이하의 정수값이 주어질 때
# 삼각형의 부분 삼각형을 이루는 모든 길이 1의 정삼각형의 값의 합중 최댓값을 구하는 문제
def sol4902():
    # i행 j열의 삼각형의 index
    index = [[-1] * 800 for _ in range(400)]
    tmp = 0
    for i in range(400):
        for j in range(i * 2 + 1):
            index[i][j] = tmp
            tmp += 1

    answer = []
    while True:
        inp = input().rstrip()

        # 0이 입력되면 종료
        if inp == '0':
            break

        # 삼각형을 이루는 값들의 누적합을 구함
        n, *tri = map(int, inp.split())
        for i in range(1, len(tri)):
            tri[i] += tri[i - 1]
        tri.append(0)

        # 부분 삼각형의 값의 최댓값
        max_value = -INF

        # 각 행, 열의 길이 1 삼각형을 꼭짓점으로 하는 부분삼각형의 값으로 max_value를 갱신
        for i in range(n):
            line_cnt = i * 2 + 1
            for j in range(line_cnt):
                # 삼각형 (i, j)의 index
                idx = index[i][j]

                # 크기 1 삼각형의 크기로 갱신
                total = tri[idx] - tri[idx - 1]
                max_value = max(max_value, total)

                # 역삼각형일 경우
                if j % 2:
                    gap = 2
                    for k in range(i - 1, -1, -1):
                        e = index[k][j]
                        s = index[k][j - gap]
                        if s == -1 or e == -1:
                            break
                        total += tri[e] - tri[s - 1]
                        max_value = max(max_value, total)
                        gap += 2

                # 역삼각형이 아닐 경우
                else:
                    gap = 2
                    for k in range(i + 1, n):
                        s = index[k][j]
                        e = index[k][j + gap]
                        if e == -1:
                            break
                        total += tri[e] - tri[s - 1]
                        max_value = max(max_value, total)
                        gap += 2
        answer.append(max_value)

    return '\n'.join([f'{i + 1}. {answer[i]}' for i in range(len(answer))])
