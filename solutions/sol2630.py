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
    # 1칸짜리 색종이일 경우
    if l == 1:
        c = int(paper[x][y])
        res[c] += 1
        return c

    nl = l // 2
    cnt = cut(paper, x, y, nl) + cut(paper, x + nl, y, nl) + cut(paper, x, y + nl, nl) + cut(paper, x + nl, y + nl, nl)
    # 잘라낸 네 부분이 모두 같은 색의 색종이였을 경우
    # 갯수가 세 번 추가로 더해졌기 때문에 3만큼 빼준다
    if cnt == 4:
        res[1] -= 3
        return 1
    elif cnt == 0:
        res[0] -= 3
        return 0

    # 모두 같은 색종이가 아닌경우
    return -4
