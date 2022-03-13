import sys
from collections import defaultdict

input = sys.stdin.readline
MAX_COST = 10 ** 9 + 1


# 1050 물약
# <물약이름> <가격> 의 형태로 n개의 물약의 상점가격이 주어지고
# <물약이름>=<재료갯수><재료이름>+<재료갯수><재료이름>+... 의 형태로 물약의 조합식이 주어졌을 때
# "LOVE"라는 이름의 물약을 만들기 위해 필요한 최소비용을 구하는 문제
# 단, LOVE를 만들 수 없다면 -1을, 최소비용이 1000000000보다 크다면 1000000001을 반환해야한다.
def sol1050():
    n, m = map(int, input().split())

    # 재료 가격 파싱
    # material[i] 은 재료 i의 상점가격
    material = dict()
    for _ in range(n):
        mt, cost = input().split()
        material[mt] = int(cost)

    # g[i] 는 재료 i를 만들기 위한 레시피와 진입차수
    g = defaultdict(list)

    # d[i] 는 조합에 재료 i를 필요로하는 재료들과 레시피 번호, 진입차수를 감소시켜야하는지 여부
    d = defaultdict(list)

    # 조합식 파싱
    for _ in range(m):
        # 조합결과 만들어지는 재료 res
        # 조합식 mat
        res, mat = input().rstrip().split("=")

        # recipe는 필요한 재료이름 mt, 필요한 갯수 cnt의 쌍으로 구성된 딕셔너리
        recipe = defaultdict(int)
        rn = len(g[res])
        for o in mat.split('+'):
            idx = 0
            while o[idx].isdigit():
                idx += 1
            mt, cnt = o[idx:], int(o[:idx])
            recipe[mt] += cnt

        # 조합식을 참조하여 g, d 를 갱신
        recipe = recipe.items()

        for mt, cnt in recipe:
            d[mt].append([res, rn, True])
        g[res].append([len(recipe), recipe])

    # 처음부터 계산 가능한 것은 상점에서 파는 재료들
    q = material.keys()

    # dp[i] 는 재료 i를 만들기 위해 필요한 최소비용
    dp = dict()
    while q:
        nq = set()
        for mat in q:
            # 갱신 여부
            changed = False

            # degree가 0인 레시피들로 자신의 값을 갱신
            for degree, recipe in g[mat]:
                if not degree:
                    # 레시피에 따라 계산한 최소비용
                    cost = sum([dp[mt] * cnt for mt, cnt in recipe])

                    # material에 mat을 얻기위한 최소비용 정보가 없었거나
                    # cost가 기존의 최소비용보다 작을 경우 이를 갱신
                    if mat not in dp or cost < dp[mat]:
                        dp[mat] = cost
                        changed = True

            # 상점 판매가로 자신의 값을 갱신
            if mat in material:
                cost = material[mat]
                if mat not in dp or cost < dp[mat]:
                    dp[mat] = cost
                    changed = True

            # dp[mat]의 값에 갱신이 발생한 경우 mat에 영향을 받는 모든 재료들의
            # degree를 감소시키고 degree가 0이라면 비용을 재계산하기 위해 큐에 삽입
            if changed:
                for link in d[mat]:
                    target, rn, dec = link
                    # 진입차수를 감소시켜야한다면 감소시키고
                    # 더이상 진입차수를 감소시킬 필요가 없음을 표시
                    if dec:
                        g[target][rn][0] -= 1
                        link[2] = False

                    # target의 레시피의 진입차수가 0이라면 target을 큐에 삽입
                    if not g[target][rn][0]:
                        nq.add(target)
        q = nq

    # LOVE 가 dp에 매핑되어있지 않다면 조합할 방법이 존재하지 않는 것이므로 -1
    # 매핑되어있다면 dp["LOVE"] 값을 반환.  단, 1000000000보다 클 경우 1000000001을 반환
    return -1 if "LOVE" not in dp else min(dp["LOVE"], MAX_COST)
