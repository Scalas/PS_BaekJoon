import sys
import math

input = sys.stdin.readline


# 3053 택시 기하학
# 유클리드 기하학에서의 원의 넓이와 택시 기하학에서의 원의 거리를 구하는 문제
def sol3053():
    PI = math.pi
    r = int(input())
    print('%.6f %.6f' % (r ** 2 * PI, 2 * r ** 2), sep='\n')
