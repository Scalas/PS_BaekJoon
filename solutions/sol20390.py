import sys


# 20390 완전 그래프의 최소 스패닝 트리
# 주어진 정점들로 이루어진 완전그래프의 최소 스패닝 트리를 구하는 문제
# 간선이 매우 많기 때문에 그래프의 상태에 영향을 받지않는 Prim's Algorithm 을 사용
# 처음에는 heapq 를 사용하여 구현했지만 메모리제한이 16mb 이기 떄문에
# 정석대로 트리로부터 정점들까지의 거리를 나타낸 배열을 갱신해나가며 가장 가까운 정점을 탐색했다.
def sol20390():
    input = sys.stdin.read
    n, a, b, c, d, *vertex = map(int, input().split())
    INF = 2000000000000

    include = [False] * n
    inq = [INF] * n
    include[0] = True
    inq[0] = 0
    res = 0
    # 시작점인 0번 정점에서 각 정점으로의 거리
    for i in range(1, n):
        inq[i] = ((vertex[0] * a + vertex[i] * b) % c) ^ d

    # n-1 개의 정점을 추가
    for i in range(n - 1):
        # 트리로부터 가장 가까운 정점을 선택
        v, dist = 0, INF
        for j in range(n):
            if not include[j] and inq[j] < dist:
                v, dist = j, inq[j]
        # 가장 가까운 정점을 트리에 포함시키고 트리와 정점들 사이의 거리를 갱신
        include[v] = True
        res += dist
        for j in range(n):
            if not include[j]:
                dst = ((vertex[v] * a + vertex[j] * b) % c) ^ d if v < j else ((vertex[j] * a + vertex[v] * b) % c) ^ d
                inq[j] = min(inq[j], dst)
    return res
