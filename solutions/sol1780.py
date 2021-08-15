import sys

input = sys.stdin.readline


# 1780 종이의 개수
# 2630 색종이 문제와 거의 같지만 종이의 변의 길이가 3의 제곱수라는 것과 자르기를 3*3으로 한다는것만 다른 문제
# 데이터의 크기가 커져서 기존에 푼 방식대로 종이를 O(N^2)으로 탐색하여 잘라야할지 판단하면 시간초과가 발생
# 판단하지 않고 종이를 잘라서 재귀호출한 뒤 그 결과를 토대로 자를 필요가 있었는지 판정
def sol1780():
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    res = [0, 0, 0]

    def check(r, c, s):
        color = paper[r][c]
        # 1칸짜리 종이라면 해당 종이 색의 카운트를 1 증가 후 종이의 색을 반환
        if s == 1:
            res[color + 1] += 1
            return color

        g = s // 3
        cut = False
        # 종이를 9등분하여 재귀호출
        for i in range(r, r + s, g):
            for j in range(c, c + s, g):
                if check(i, j, g) != color:
                    cut = True

        # 쪼갠 종이들이 모두 같은 색이 아니었다면 2 반환
        if cut:
            return 2

        # 모두 같은 색이었다면 중복으로 더해진 갯수를 빼준 뒤 색(-1, 0, 1) 반환
        res[color + 1] -= 8
        return color

    check(0, 0, n)
    return '\n'.join(map(str, res))
