import sys

input = sys.stdin.readline


# 20040 사이클 게임
# 주어진 점들을 선분으로 이어나가며 사이클이 생기는 차례를 구하는 문제
# 사이클이 생기려면 이미 같은 집합(네트워크)에 속해있는 점끼리 이어져야 한다.
# 이를 이용하면 유니온 파인드를 통해 간단히 해결 가능하다.
def sol20040():
    n, m = map(int, input().split())
    u = [-1] * (n + 1)
    check = 0
    for turn in range(1, m + 1):
        s, e = map(int, input().split())
        if not union(u, s, e):
            check = turn
            break

    return check


def union(u, a, b):
    a = find(u, a)
    b = find(u, b)
    if a == b:
        return False
    if u[a] < u[b]:
        u[a] += u[b]
        u[b] = a
    else:
        u[b] += u[a]
        u[a] = b
    return True


def find(u, x):
    if u[x] < 0:
        return x
    u[x] = find(u, u[x])
    return u[x]
