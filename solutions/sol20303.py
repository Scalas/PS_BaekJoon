import sys

input = sys.stdin.readline


# 20303 할로윈의 양아치
# n명의 아이와 아이들간의 친구관계가 주어지고 한명의 아이에게 사탕을 뺏으면
# 그 아이와 친구관계로 이어진 모든 아이에게서 사탕을 뺏어야하며
# 사탕을 뺏긴 아이가 k명 이상이 되어선 안될 때
# 얻을 수 있는 사탕의 최대 수를 구하는 문제
def sol20303():
    n, m, k = map(int, input().split())
    candy = list(map(int, input().split()))
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    # 친구관계 클러스터의 크기와 클러스터별 얻을 수 있는 사탕 갯수를 구함
    items = []
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            q = [i]
            visited[i] = True
            candy_cnt = candy[i - 1]
            kids_cnt = 1
            while q:
                nq = []
                for cur in q:
                    for nxt in g[cur]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            candy_cnt += candy[nxt - 1]
                            kids_cnt += 1
                            nq.append(nxt)
                q = nq
            items.append([kids_cnt, candy_cnt])

    # knap-sack문제와 같은 요령으로 최대 가치를 얻는 경우를 구함
    d = {0: 0}
    for w, v in items:
        for pw, pv in d.copy().items():
            nw, nv = w + pw, v + pv
            if nw >= k:
                continue
            d[nw] = max(d.get(nw, 0), nv)

    return max(d.values())
