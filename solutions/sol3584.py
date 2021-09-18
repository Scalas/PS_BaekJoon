import sys

input = sys.stdin.readline


# 3584 가장 가까운 공통 조상
# 노드의 수가 적고 쿼리도 케이스당 하나 뿐이기 때문에
# 단순한 방식으로도 해결 가능

# 1. 조상 노드 리스트를 비교하는 방식으로 구현
def sol3584_1():
    # 케이스별 정답 리스트
    answer = []
    for t in range(int(input())):
        # 노드의 수
        n = int(input())

        # 각 노드의 부모노드
        parent = [0] * (n + 1)

        # 부모노드와 자식노드를 입력받아 부모노드를 채운다
        for _ in range(n - 1):
            a, b = map(int, input().split())
            parent[b] = a

        # 가장 가까운 공통조상을 구할 두 노드
        u, v = map(int, input().split())

        # 두 노드의 조상 노드 리스트를 구한다.
        up, vp = [], []
        while u:
            up.append(u)
            u = parent[u]
        while v:
            vp.append(v)
            v = parent[v]

        # 두 노드의 조상 노드 리스트를 뒤집는다.
        up, vp = up[::-1], vp[::-1]

        # 루트 노드부터 시작하여 두 노드의 조상 노드가 서로 달라질 때 까지 탐색
        # 두 노드의 조상 노드가 마지막으로 같았을 때의 조상 노드가 가장 가까운 공통 조상 노드가 된다.
        res = 0
        for i in range(min(len(up), len(vp))):
            if up[i] == vp[i]:
                res = up[i]
            else:
                break

        # 정답 리스트에 결과 삽입
        answer.append(res)

    # 출력 형식에 맞춰 정답 리스트 반환
    return '\n'.join(map(str, answer))


# 2. 두 노드의 깊이를 동일하게 맞춘 뒤 공통 조상 노드를 만날 때 까지 거슬러올라가는 방식
#    이후에 sparse table 을 적용하기 위한 전 단계 알고리즘
def sol3584_2():
    # 정답 리스트
    answer = []

    # 테스트케이스
    for t in range(int(input())):
        # 노드의 수
        n = int(input())

        # 그래프 생성, 부모 노드 구하기
        g = [[] for _ in range(n + 1)]
        parent = [0] * (n + 1)
        for _ in range(n - 1):
            a, b = map(int, input().split())
            g[a].append(b)
            parent[b] = a

        # 루트 노드로부터 bfs탐색으로 각 노드의 깊이를 구한다
        depth = [0] * (n + 1)
        root = [i for i in range(1, n + 1) if not parent[i]][0]

        q = [root]
        while q:
            nq = []
            for cur in q:
                for c in g[cur]:
                    depth[c] = depth[cur] + 1
                    nq.append(c)
            q = nq

        # 주어진 두 노드 u, v
        u, v = map(int, input().split())

        # 노드 u의 깊이가 노드 v의 깊이보다 크도록 한다.
        if depth[u] < depth[v]:
            u, v = v, u

        # 두 노드의 깊이차가 0이 될 때 까지 깊은 쪽 노드인 u를 끌어올린다
        while depth[u] - depth[v]:
            u = parent[u]

        # 두 노드가 서로 같아질 때 까지 두 노드를 끌어올린다
        while u != v:
            u, v = parent[u], parent[v]

        # u와 v가 서로 같아지면 u == v == 가장 가까운 공통 조상 노드 가 된다.
        answer.append(u)

    # 출력 형식에 맞춰 정답 리스트 반환
    return '\n'.join(map(str, answer))
