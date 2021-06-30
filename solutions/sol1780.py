import sys

input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
res = [0, 0, 0]


# 1780 종이의 개수
# 2630 색종이 문제와 거의 같지만 종이의 변의 길이가 3의 제곱수라는 것과 자르기를 3*3으로 한다는것만 다른 문제
# 데이터의 크기가 커져서 기존에 푼 방식대로 종이를 O(N^2)으로 탐색하여 잘라야할지 판단하면 시간초과가 발생
# 판단하지 않고 종이를 잘라서 재귀호출한 뒤 그 결과를 토대로 자를 필요가 있었는지 판정
def sol1780():
    cut(0, 0, n)
    print('\n'.join(map(str, res)))


def cut(x, y, l):
    # 1칸짜리 종이라면 해당 종이 색의 카운트를 1 증가 후 종이의 색을 반환
    if l == 1:
        res[paper[x][y]+1] += 1
        return paper[x][y]

    # 종이를 9조각으로 분할, 결과를 저장
    nl = l // 3
    p = []
    for i in range(3):
        for j in range(3):
            p.append(cut(x+nl*i, y+nl*j, nl))

    # 비교를 위한 첫번쨰 조각의 결과
    check = p[0]

    # 만약 첫번째 조각이 모두 같은색인 종이가 아니었다면
    if check == -2:
        return -2

    for i in p[1:]:
        # 하나의 조각라도 다른 결과가 나왔다면 현재 종이는 모두 같은색이 아님(-2 반환)
        if i != check:
            return -2

    # 모두 같은색인 종이였다면 분할하지 않아도 될 종이를 분할하여 추가로 카운트된 종이의 수만큼 카운트를 감소
    # 1로 끝날 카운트가 9칸치 상승했기 때문에 -8
    res[check+1] -= 8

    # 종이 색을 반환
    return check
