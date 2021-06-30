import sys

input = sys.stdin.readline
n = int(input())
video = [input() for _ in range(n)]


# 2630 쿼드트리
# 2의 제곱수를 변의 길이로 가지는 정사각형 배열로 표현된 영상에서
# 색이 다른 칸이 있는 경우 같은크기의 정사각형 배열 4개로 4등분
# 각각의 잘린 배열에서 같은 작업을 반복수행하여 데이터를 압축하는 문제
# 2630 색종이 문제와 사실상 같은 문제
def sol1992():
    answer = cut((0, n), (0, n))
    sys.stdout.write(answer)


def cut(r, c):
    global video
    color = video[r[0]][c[0]]
    check = False
    for i in range(r[0], r[1]):
        for j in range(c[0], c[1]):
            if (video[i][j] != color):
                check = True
                break
        if (check):
            break
    if (check):
        mr = r[0] + (r[1] - r[0]) // 2
        mc = c[0] + (c[1] - c[0]) // 2
        return (f'({cut((r[0], mr), (c[0], mc))}{cut((r[0], mr), (mc, c[1]))}{cut((mr, r[1]), (c[0], mc))}{cut((mr, r[1]), (mc, c[1]))})')
    else:
        return color


# 해당 범위의 색이 모두 같은 경우의 처리를 조금 달리한 풀이
# 매번 범위의 크기만큼 반복문을 돌리지 않고 네 구역의 반환값이 모두 같은지를 검사하는 방식
def sol1992_2():
    n = int(input())
    paper = [list(input()) for _ in range(n)]
    print(cut_2(paper, 0, 0, n))


def cut_2(paper, x, y, l):
    # 점 하나일 경우
    if l == 1:
        return paper[x][y]

    nl = l // 2
    res = [cut_2(paper, x, y, nl), cut_2(paper, x, y + nl, nl), cut_2(paper, x + nl, y, nl), cut_2(paper, x + nl, y + nl, nl)]
    # 잘라낸 네 부분이 모두 같은 색의 점인 경우
    c = res[0]
    if c[0]=='(':
        return '(' + ''.join(res) + ')'
    for i in res[1:]:
        if i != c:
            return '(' + ''.join(res) + ')'
    return c
