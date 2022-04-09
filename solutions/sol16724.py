import sys

input = sys.stdin.readline


def sol16724():
    n, m = map(int, input().split())
    size = n * m
    direction = {'U':-m, 'D':m, 'L':-1, 'R':1}

    # 연결된 칸들을 집합으로 묶음
    u = [-1] * size
    board = ''.join(sys.stdin.read().split())
    for i in range(size):
        union(u, i, i + direction[board[i]])

    # 집합의 갯수 반환
    answer = 0
    for i in u:
        if i < 0:
            answer += 1
    return answer


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


def find(u, x):
    if u[x] < 0:
        return x
    u[x] = find(u, u[x])
    return u[x]
