import sys

input = sys.stdin.readline


# 3584 가장 가까운 공통 조상
# 노드의 수가 적고 쿼리도 케이스당 하나 뿐이기 때문에
# 단순한 방식으로도 해결 가능
def sol3584():
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
