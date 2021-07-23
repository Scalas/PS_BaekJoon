import sys

input = sys.stdin.readline


# 4195 친구 네트워크
# 친구관계 (연결관계)가 주어질 때마다 친구네트워크의 크기, 즉 친구가 된 둘이 속한 친구집합의 크기를 구하는 문제
# 유니온 파인드 알고리즘을 활용하여 쉽게 해결 가능하다.
def sol4195():
    answer = []
    for t in range(int(input())):
        friend = {}
        u = []
        res = []
        for _ in range(int(input())):
            a, b = input().split()
            if a not in friend:
                friend[a] = len(friend)
                u.append(-1)
            if b not in friend:
                friend[b] = len(friend)
                u.append(-1)
            a = find(u, friend[a])
            b = find(u, friend[b])
            res.append(-union(u, a, b))
        answer.append('\n'.join(map(str, res)))
    return '\n'.join(answer)


def union(u, a, b):
    a = find(u, a)
    b = find(u, b)
    if a != b:
        if u[a] < u[b]:
            u[a] += u[b]
            u[b] = a
            return u[a]
        else:
            u[b] += u[a]
            u[a] = b
            return u[b]
    return u[a]


def find(u, x):
    if u[x] < 0:
        return x
    u[x] = find(u, u[x])
    return u[x]
