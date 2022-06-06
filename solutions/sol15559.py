import sys

input = sys.stdin.readline


# 15559 내 선물을 받아줘
# n * m 격자형 공간과 각 칸에서의 대상의 이동 방향이 주어질 때
# 대상이 어느칸에서 출발하더라도 반드시 선물을 둔 칸을 지나게 하기 위해 필요한 선물의 최소 갯수를 구하는 문제
# 분리집합을 사용하여 해결 가능
def sol15559():
    n, m = map(int, input().split())
    board = ''.join([input().rstrip() for _ in range(n)])
    u = [-1] * (n * m)
    for i in range(n * m):
        if board[i] == 'N':
            union(u, i, i - m)

        elif board[i] == 'S':
            union(u, i, i + m)

        elif board[i] == 'W':
            union(u, i, i - 1)

        elif board[i] == 'E':
            union(u, i, i + 1)

    answer = 0
    for i in range(len(u)):
        if u[i] < 0:
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
