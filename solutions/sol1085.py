import sys

input = sys.stdin.readline


# 1085 직사각형에서 탈출
# 직사각형 내부의 점에서 직사각형의 변으로 가기위한 최단거리를 구하는 문제
def sol1085():
    x, y, w, h = map(int, input().split())
    print(min(x, y, w - x, h - y))

