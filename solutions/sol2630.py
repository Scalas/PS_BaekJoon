import sys

input = sys.stdin.readline
res = [0, 0]

# 2630 색종이 만들기
# 2의 제곱수를 변의 길이로 가지는 정사각형 색종이를
# 모든 색이 같지 않을 경우 같은 크기의 정사각형 네개로 자르는 작업을 반복하여
# 더이상 자를 수 없게 됐을 때 색상별 색종이의 수를 구하는 문제
# 색종이의 범위를 매개변수로 재귀함수를 호출하여 해결할 수 있다
def sol2630():
    n = int(input())
    paper = [input().split() for _ in range(n)]
    cut(paper, 0, 0, n)
    print('\n'.join(map(str, res)))


def cut(paper, x, y, l):
    check = paper[x][y]
    # 색종이의 색이 다른 부분이 하나라도 있으면 check 값을 -1로 하고 break
    for i in range(x, x + l):
        for j in range(y, y + l):
            if paper[i][j] != check:
                check = -1
                break

    # 색종이가 한 가지 색으로 칠해져있는 경우
    if check != -1:
        res[int(check)] += 1
        return

    # 잘라야할 경우
    nl = l // 2
    cut(paper, x, y, nl)
    cut(paper, x + nl, y, nl)
    cut(paper, x, y + nl, nl)
    cut(paper, x + nl, y + nl, nl)
