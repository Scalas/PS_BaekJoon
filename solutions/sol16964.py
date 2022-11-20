import sys

input = sys.stdin.readline


# 16964 DFS 스페셜 저지
# n 개의 노드로 구성된 트리와 순회 노드 리스트가 순서대로 주어졌을 때
# 주어진 순회 리스트가 DFS 순회의 순서를 따르는지 확인하는 문제
def sol16964():
    n = int(input())
    g = [set() for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].add(v)
        g[v].add(u)

    # 1번 노드가 루트이므로 1번부터 시작하지 않으면 잘못된 순회
    traversal = list(map(int, input().split()))
    if traversal[0] != 1:
        return 0

    idx = 1
    visited = [False] * (n + 1)

    def dfs(cur):
        nonlocal idx

        visited[cur] = True

        # 인접한 다음 노드가 없다면 현재까진 올바른 순서대로 순회중
        if not g[cur]:
            return 1

        while g[cur]:
            # 모든 순회 리스트를 방문하는데 성공했다면 올바른 DFS 순회 리스트
            if idx == n:
                return 1

            nxt = traversal[idx]
            # 다음 순회해야할 노드가 인접 노드중에 존재한다면 진행
            if nxt in g[cur]:
                g[cur].remove(nxt)
                idx += 1
                # 진행중 한번이라도 잘못된 순회임이 밝혀지면 바로 0 반환
                if not dfs(nxt):
                    return 0
            # 존재하지 않을 경우 더이상 방문 가능한 인접 노드가 없어야함
            # 만약 하나라도 존재한다면 DFS 순회가 아니기 때문에 0 반환
            else:
                for nxt_cand in g[cur]:
                    if not visited[nxt_cand]:
                        return 0
                break
        # 방문 가능한 인접노드를 모두 방문하고 순회방식에 문제가 없을 경우 1 반환
        return 1
    
    # 1번 노드부터 방문시작
    return dfs(1)
