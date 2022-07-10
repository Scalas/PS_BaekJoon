import sys

input = sys.stdin.readline


# 1800 인터넷 설치
# n명의 학생간의 연결관계와 비용이 p개 주어지고
# k개까지의 인터넷 연결비용을 무료로 할 수 있으며
# k개의 무료 연결을 제외한 인터넷 연결비용중 최댓값만을 지불한다고 할 때
# 0번 학생과 n - 1번 학생을 연결하는데 드는 최소비용을 구하는 문제
def sol1800():
    n, p, k = map(int, input().split())

    # 학생이 한명뿐인 경우 비용이 들지 않음
    if n == 1:
        return 0

    # 학생들간의 연결정보
    g = [[] for _ in range(n)]

    # 간선의 길이 집합
    edges = set()

    for _ in range(p):
        u, v, w = map(int, input().split())
        g[u - 1].append([v - 1, w])
        g[v - 1].append([u - 1, w])
        edges.add(w)

    # 최대비용이 max_cost를 넘지않으면서 n번 컴퓨터에 인터넷을 연결할 수 있는지 확인
    def go(max_cost):
        visited = [[False] * (k + 1) for _ in range(n)]
        q = [(0, k)]
        while q:
            nq = []
            for cur, fc in q:
                for nxt, dst in g[cur]:
                    # 인터넷선의 가격이 max_cost를 넘기지 않는 경우
                    # 무료케이블 찬스를 쓰지 않아도 됨
                    if dst <= max_cost:
                        if nxt == n - 1:
                            return True
                        if not visited[nxt][fc]:
                            visited[nxt][fc] = True
                            nq.append((nxt, fc))

                    # 인터넷선의 가격이 max_cost보다 높고 무료 케이블 찬스가 남아있는 경우
                    # 무료케이블 찬스를 써야함
                    elif fc > 0:
                        if nxt == n - 1:
                            return True
                        if fc > 0 and not visited[nxt][fc - 1]:
                            visited[nxt][fc - 1] = True
                            nq.append((nxt, fc - 1))
            q = nq

        # 탐색이 끝날 때 까지 마지막 노드에 도달하지 못했을 경우
        # 최대 비용 max_cost로는 마지막 노드에 도달 불가
        return False

    edges.add(0)
    edges = sorted(edges)

    # 최대비용으로 마지막 노드에 도달 가능한지 확인
    if not go(edges[-1]):
        return -1

    # 이분탐색으로 마지막 노드에 도달 가능한 최대비용의 최솟값을 구함
    s, e = 0, len(edges)
    while s < e:
        mid = (s + e) // 2
        if go(edges[mid]):
            e = mid
        else:
            s = mid + 1

    return edges[e]
