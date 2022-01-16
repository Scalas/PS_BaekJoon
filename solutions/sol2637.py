import sys

input = sys.stdin.readline


# 2637 장난감 조립
# 완제품의 번호 n이 주어졌을 때, 다른 부품으로 만들 수 없는 부품을 기본부품이라 하고
# 완제품이 아닌 부품중 다른 부품으로 조립 가능한것을 중간부품이라 한다.
# 중간부품들을 조립하기 위해 필요한 기본부품, 중간부품과 그 수가 주어졌을 때
# 완제품을 만들기 위해 필요한 기본 부품의 종류별 갯수를 구하는 문제
def sol2637():
    n = int(input())
    m = int(input())

    # g[i] 는 조립을 위해 i번 부품을 필요로하는 부품의 리스트
    # degree[i]는 i번 부품을 조립하기 위해 필요한 기본부품, 혹은 중간부품의 종류의 수 = 진입차수
    g = [[] for _ in range(n+1)]
    degree = [0] * (n+1)
    for _ in range(m):
        u, v, w = map(int, input().split())
        degree[u] += 1
        g[v].append((u, w))

    # dp[i][j] 는 i 번 부품을 만들기 위해 필요한 기본부품 j의 갯수
    dp = [[0] * (n+1) for _ in range(n+1)]

    # 초기 진입차수가 0인 부품을 탐색(기본부품)
    base = []
    for p in range(1, n+1):
        if not degree[p]:
            base.append(p)
            dp[p][p] = 1

    q = base[:]
    while q:
        nq = []
        # 제작에 필요한 기본 부품 갯수를 알고있는 부품 p에 대해
        for p in q:
            # p로 만들 수 있는 부품과 필요한 갯수
            for nxt, cnt in g[p]:
                # nxt를 만들기 위해 필요한 기본부품의 갯수에
                # p를 만들기 위해 필요한 기본부품의 갯수 * cnt를 더함
                for bp in base:
                    dp[nxt][bp] += dp[p][bp] * cnt

                # nxt 부품의 진입차수를 1 줄이고 만약 0이됐다면 큐에 추가
                degree[nxt] -= 1
                if not degree[nxt]:
                    nq.append(nxt)
        q = nq

    # 완제품 조립에 필요한 기본부품의 종류와 갯수를 반환
    return '\n'.join(['%d %d' % (b, dp[n][b]) for b in base])
