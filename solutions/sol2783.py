import sys

input = sys.stdin.readline


# 2783 삼각 김밥
# 1000그람의 삼각김밥을 사기 위한 최소비용을 구하는 문제
def sol2783():
    x, y = map(int, input().split())
    for _ in range(int(input())):
        u, v = map(int, input().split())
        if u / v < x / y:
            x, y = u, v
    return '%.2f' % ((x / y) * 1000)
