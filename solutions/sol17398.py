import sys

input = sys.stdin.readline


# 17398 통신망 분할
# n개의 통신탑과 m개의 연결이 주어지고 그중 q개의 연결을 순서대로 끊기 위한 비용의 총합을 구하는 문제
# 연결을 끊을 때의 비용은 연결을 끊는 것으로 통신탑의 그룹이 두 그룹으로 나눠졌을 때 두 그룹의 크기의 곱이 된다.
# 만약 연결을 끊어도 통신탑이 두 그룹으로 나눠지지 않을 경우 비용은 0이된다.
def sol17398():
    n, m, q = map(int, input().split())
    u = [-1] * (n + 1)
    edges = [list(map(int, input().split())) for _ in range(m)]
    div = [int(input()) for _ in range(q)]
    div_set = set(div)

    # 제거되지 않는 연결들에 대해 union 처리
    for i in range(m):
        if (i+1) in div_set:
            continue
        union(u, edges[i][0], edges[i][1])

    # 연결을 끊는데 들어가는 비용
    answer = 0

    # 제거할 연결을 역순으로 union
    for i in range(q-1, -1, -1):
        answer += union(u, edges[div[i]-1][0], edges[div[i]-1][1])

    return answer


def union(u, a, b):
    a = find(u, a)
    b = find(u, b)

    # union할 두 그룹의 크기의 곱
    res = u[a] * u[b]

    if a != b:
        if u[a] < u[b]:
            u[a] += u[b]
            u[b] = a
        else:
            u[b] += u[a]
            u[a] = b

        return res
    return 0


def find(u, x):
    if u[x] < 0:
        return x
    u[x] = find(u, u[x])
    return u[x]
