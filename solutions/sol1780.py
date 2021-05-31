import sys

input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0, 0]


# 1780 종이의 개수
# 2630 색종이 문제와 거의 같지만 종이의 변의 길이가 3의 제곱수라는 것과 자르기를 3*3으로 한다는것만 다른 문제
# 데이터의 크기가 커져서 기존에 푼 방식대로 종이를 O(N^2)으로 탐색하여 잘라야할지 판단하면 시간초과가 발생
# 판단하지 않고 종이를 잘라서 재귀호출한 뒤 그 결과를 토대로 자를 필요가 있었는지 판정
def sol1780():
    cut((0, n), (0, n))
    print(*answer, sep='\n')


def cut(r, c):
    global paper
    global answer

    # 1칸짜리 종이라면 해당 종이 색의 카운트를 1 증가 후 종이의 색을 반환
    if (r[1] - r[0] == 1):
        answer[paper[r[0]][c[0]] + 1] += 1
        return paper[r[0]][c[0]]

    # 종이를 9조각으로 분할, 결과를 저장
    pieces = []
    for i in range(3):
        for j in range(3):
            nr = (r[0] + i * ((r[1] - r[0]) // 3), r[0] + (i + 1) * ((r[1] - r[0]) // 3))
            nc = (c[0] + j * ((c[1] - c[0]) // 3), c[0] + (j + 1) * ((c[1] - c[0]) // 3))
            pieces.append(cut(nr, nc))

    # 비교를 위한 첫번쨰 조각의 결과
    start = pieces[0]

    # 만약 첫번째 조각이 모두 같은색인 종이가 아니었다면
    # 현재 종이도 모두 같은색이 아님(-2 반환)
    if (start == -2):
        return -2

    for piece in pieces[1:]:
        # 하나의 조각라도 다른 결과가 나왔다면 현재 종이는 모두 같은색이 아님(-2 반환)
        if (piece != start):
            return -2

    # 모두 같은색인 종이였다면 분할하지 않아도 될 종이를 분할하여 추가로 카운트된 종이의 수만큼 카운트를 감소
    # 1로 끝날 카운트가 9칸치 상승했기 때문에 -8
    answer[start + 1] -= 8

    # 종이 색을 반환
    return start

# C++ 등의 언어였다면 단순히 먼저 조건을 확인한 후 분할하여도 시간초과는 되지 않았을 것으로 추정
# 파이썬이 문제풀이에 유리한 언어이긴 하지만 이런 경우에 느린 속도가 발목을 잡을 수 있음
# 보조언어로 C++ 등을 익혀둘것
