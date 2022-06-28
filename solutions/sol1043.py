import sys

input = sys.stdin.readline


# 1043 거짓말
# m개의 파티에 n명의 사람들이 참여하고 n명의 사람들중 t명의 진실을 아는 사람들이 있을 때
# 진실을 아는 사람에게 직/간접적으로 진실을 들을 일이 없었던 사람들만 참여하는 파티의 수를 구하는 문제
def sol1043():
    n, m = map(int, input().split())
    t, *tlist = map(int, input().split())

    # 파티에서 만난 사람들끼리 하나의 집합으로 연결
    u = [-1] * (n + 1)
    party = []
    for _ in range(m):
        p, *plist = map(int, input().split())
        party.append(plist)
        for i in range(p - 1):
            union(u, plist[i], plist[i + 1])

    # 진실을 아는 사람이 속한 그룹
    tp = set()
    for num in tlist:
        tp.add(find(u, num))

    # tp의 그룹에 속하지 않는 사람만이 참여한 파티의 수를 구함
    answer = 0
    for p in party:
        check = True
        for num in p:
            if find(u, num) in tp:
                check = False
                break
        if check:
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
