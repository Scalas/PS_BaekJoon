import sys

input = sys.stdin.readline


# 2458 키 순서
# n명의 학생이 있고 그중 m쌍의 학생의 키의 대소관계가 주어졌을 때
# 자신이 n명의 학생중 키순서로 몇 번째인지 정확히 알 수 있는 학생의 수를 구하는 문제
def sol2458():
    n, m = map(int, input().split())
    larger = [[] for _ in range(n)]
    smaller = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        larger[u - 1].append(v - 1)
        smaller[v - 1].append(u - 1)

    smaller_set = [set() for _ in range(n)]
    larger_set = [set() for _ in range(n)]
    
    def dfs_smaller(cur, start):
        visited[cur] = True
        if cur != start:
            smaller_set[cur].add(start)
        for nxt in larger[cur]:
            if visited[nxt]:
                continue
            dfs_smaller(nxt, start)

    def dfs_larger(cur, start):
        visited[cur] = True
        if cur != start:
            larger_set[cur].add(start)
        for nxt in smaller[cur]:
            if visited[nxt]:
                continue
            dfs_larger(nxt, start)
    
    # 각 학생보다 작은 학생의 수, 큰 학생의 수를 구하여
    # 그 합과 자기자신(1)을 더한 값이 n인 경우
    # 모든 학생에 대해 자신보다 큰지 작은지 여부를 알기 때문에 순서를 명확히 알 수 있음
    for i in range(n):
        visited = [False] * n
        dfs_larger(i, i)
        visited = [False] * n
        dfs_smaller(i, i)

    return len([i for i in range(n) if len(smaller_set[i]) + len(larger_set[i]) + 1 == n])
