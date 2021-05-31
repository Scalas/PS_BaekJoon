import sys

input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0]


# 2630 색종이 만들기
# 2의 제곱수를 변의 길이로 가지는 정사각형 색종이를
# 모든 색이 같지 않을 경우 같은 크기의 정사각형 네개로 자르는 작업을 반복하여
# 더이상 자를 수 없게 됐을 때 색상별 색종이의 수를 구하는 문제
# 색종이의 범위를 매개변수로 재귀함수를 호출하여 해결할 수 있다
def sol2630():
    # 색종이 전체범위에서 자르기 시작
    cut((0, n), (0, n))
    print(answer)


def cut(r, c):
    global paper
    global answer

    # 색종이의 색이 다른 부분이 하나라도 있으면 check 값을 참으로 하고 break
    color = paper[r[0]][c[0]]
    check = False
    for i in range(r[0], r[1]):
        for j in range(c[0], c[1]):
            if (paper[i][j] != color):
                check = True
                break
        if (check):
            break

    # 색종이가 한 가지 색으로 칠해져있지 않은 경우(잘라야할 경우)
    if (check):
        # 가로/세로 중간지점
        mr = r[0] + (r[1] - r[0]) // 2
        mc = c[0] + (c[1] - c[0]) // 2

        # 잘라진 네개의 색종이의 범위를 매개변수로 재귀호출
        cut((r[0], mr), (c[0], mc))
        cut((mr, r[1]), (c[0], mc))
        cut((r[0], mr), (mc, c[1]))
        cut((mr, r[1]), (mc, c[1]))

    # 색종이가 한 가지 색으로 칠해져있는 경우(자를 필요가 없는 경우)
    # 해당 색상의 색종이 수 +1
    else:
        answer[color] += 1
