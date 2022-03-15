import sys

input = sys.stdin.readline
INF = 10 ** 9


# 16562 친구비
# n명의 학생과 각 학생이 요구하는 친구비, 각 학생들간의 친구관계가 주어지고
# 어떤 학생과 친구가 될 경우 그 학생의 친구들과는 자동으로 친구가 된다고 할 때
# 모든 학생과 친구가 되기 위해 필요한 최소 비용을 구하는 문제.
# 단, 가진 돈 k가 최소비용보다 작을 경우 "Oh, no"를 반환
def sol16562():
    n, m, k = map(int, input().split())
    cost = list(map(int, input().split()))

    # disjoint set을 사용하여 친구관계인 학생들을 하나의 집합으로 묶음
    u = [-1] * n
    for _ in range(m):
        v, w = map(int, input().split())
        union(u, v-1, w-1)

    # dp[parent]는 최상위 노드가 parent인 학생들의 집합을 친구로 만들기 위한 최소비용
    # 즉, 친구집단에 속한 학생중 요구하는 친구비가 가장 적은 학생의 친구비
    dp = dict()
    for i in range(n):
        group = find(u, i)
        dp[group] = min(dp.get(group, INF), cost[i])

    # dp에 존재하는 모든 그룹의 최소 친구비를 합친 값이
    # 모든 학생과 친구가 되기위한 최소비용
    total_cost = sum(dp.values())

    # 가진돈 k보다 필요한 친구비가 많다면 "Oh no"를, 그렇지 않다면 필요한 친구비를 반환
    return "Oh no" if total_cost > k else total_cost


# union
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


# find
def find(u, x):
    if u[x] < 0:
        return x
    u[x] = find(u, u[x])
    return u[x]
