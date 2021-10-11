import sys

input = sys.stdin.readline


# 1939 중량제한
# n 개의 섬과 그 사이의 다리와 중량제한에 대한 정보가 주어졌을때
# 섬 A에서 B 사이에서 한번에 옮길 수 있는 화물의 최대중량을 구하는 문제


# 풀이1. 화물의 중량범위에 대해 이분탐색을 실행한 후 mid 값 이상의 경로만을 거쳐 섬 A에서 B로 갈수있는지 검증
# 불가능하다면 탐색범위를 하향조정, 가능하다면 상향조정
# bfs 와 이분탐색을 통한 풀이이다.
def sol1939():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    s, e = 10 ** 9, 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a].append([b, c])
        g[b].append([a, c])
        s = min(s, c)
        e = max(e, c)
    u, v = map(int, input().split())

    while s <= e:
        mid = (s + e) // 2
        res = simulate(g, u, v, mid)
        if res:
            s = mid + 1
        else:
            e = mid - 1

    return s - 1


def simulate(g, u, v, c):
    visit = [False] * len(g)
    q = [u]
    visit[u] = True
    while q:
        nq = []
        for cur in q:
            for nxt, w in g[cur]:
                if not visit[nxt] and w >= c:
                    if nxt == v:
                        return True
                    visit[nxt] = True
                    nq.append(nxt)
        q = nq
    return False



#풀이 2. union-find 를 활용한 풀이 3일 후 이 방식을 사용하여 다시 풀어볼것.