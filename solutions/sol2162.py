import sys

input = sys.stdin.readline


# 2162 선분 그룹
# 시작점의 좌표와 끝 점의 좌표로 이루어진 선분의 정보가 N개 주어지고
# 서로 교차하는 선분은 하나의 그룹이 된다고 할 때, 선분의 그룹의 갯수와 가장 큰 그룹의 크기를 구하는 문제.
def sol2162():
    # 선분의 갯수
    n = int(input())

    # 선분의 그룹을 관리하기 위한 union 리스트
    u = [-1] * n

    # 선분들의 정보
    lines = [[*map(int, input().split())] for i in range(n)]

    # 선분 그룹의 갯수 - 선분의 갯수로 초기화
    cnt = n

    # 선분 리스트에서 두 선분을 뽑는 모든 경우의 수를 따져
    # 두 선분의 교차여부를 검증
    # 두 선분이 교차한다면 union 연산을 통해 그룹짓는다
    for i in range(n):
        for j in range(i + 1, n):
            if cross_check(lines[i], lines[j]):
                # union의 결과를 선분 그룹의 갯수에 반영
                cnt += union(u, i, j)

    # 선분 그룹의 갯수와 가장 큰 그룹의 크기 반환
    return str(cnt) + '\n' + str(-min(u))


# 선분의 교차 검증 함수
def cross_check(l1, l2):
    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2
    v1, v2 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4), ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    return v1 <= 0 and v2 <= 0 and min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)


# CCW 함수
def ccw(x1, y1, x2, y2, x3, y3):
    res = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    return 1 if res > 0 else -1 if res < 0 else 0


# union 연산
def union(u, a, b):
    a = find(u, a)
    b = find(u, b)
    if a != b:
        if u[a] < u[b]:
            u[a] += u[b]
            u[b] = a
        else:
            u[b] += u[a]
            u[a] = b
        return -1
    return 0


# find 연산
def find(u, x):
    if u[x] < 0:
        return x
    u[x] = find(u, u[x])
    return u[x]
