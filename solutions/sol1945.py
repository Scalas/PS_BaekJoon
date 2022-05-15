import sys
from collections import defaultdict

input = sys.stdin.readline


# 1945 직사각형
# n개의 직사각형의 왼쪽 아래 좌표와 오른쪽 위 좌표가 주어졌을 때
# 원점을 지나는 직선이 교차할 수 있는 직사각형의 최대 갯수를 구하는 문제
# 단, 주어지는 좌표는 모두 10억 이하의 자연수이다
def sol1945():
    n = int(input())

    # sin[i]는 원점을 지나는 직선의 기울기가 i일 때 교차하기 시작하는 직사각형의 갯수
    sin = defaultdict(int)

    # sout[i]는 원점을 지나는 직선의 기울기가 i일 때 마지막으로 교차하는 직사각형의 갯수(이후 교차하지 않는)
    sout = defaultdict(int)

    # 교차하는 직사각형의 갯수에 변화가 발생할 가능성이 있는 모든 기울기값의 집합
    inc = set()

    for _ in range(n):
        u, v, w, x = map(int, input().split())

        # 사각형이 나타나는 가장 낮은 기울기는 오른쪽 아래 꼭짓점을 통과하는 직선의 기울기
        sin[v / w] += 1

        # 사각형이 나타나는 가장 높은 기울기는 왼쪽 위 꼭짓점을 통과하는 직선의 기울기
        sout[x / u] += 1

        # 기울기 set 추가
        inc.add(v / w)
        inc.add(x / u)

    answer = 0

    # 각 기울기의 교차하는 사각형 갯수중 최댓값을 구함
    square = 0
    for i in sorted(inc):
        # 사각형이 시작되는 기울기라면 사각형 갯수 증가
        if sin[i]:
            square += sin[i]

        # 교차할 수 있는 사각형의 최대갯수 갱신
        answer = max(answer, square)

        # 사각형이 끝나는 기울기라면 사각형 갯수 감소
        if sout[i]:
            square -= sout[i]

    # 교차할 수 있는 사각형의 최대갯수 반환
    return answer
