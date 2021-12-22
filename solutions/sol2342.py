import sys
from collections import defaultdict

input = sys.stdin.readline


# 2342 Dance Dance Revolution
# 중앙발판(0)에 두 발을 올려둔채로 시작하여
# 상(1), 하(3), 좌(2), 우(4) 발판을 주어진 명령대로 밟았을 때
# 들어가는 힘의 최솟값을 구하는 문제
# 상 - 하 / 좌 - 우 의 이동은 4의 힘을 소모
# 중앙에서 다른 발판으로의 이동은 2의 힘을 소모
# 인접한 발판(상 - 좌 / 상 - 우 등)으로의 이동은 3의 힘을 소모
# 이동없이 같은 발판을 밟는데는 1의 힘을 소모
def sol2342():
    cmds = list(map(int, input().split()))[:-1]
    n = len(cmds)

    # (0, 0)에서 시작하여 가능한 경우의 수를 따져나간다
    dp = defaultdict(int)
    dp[(0, 0)] = 0
    for c in cmds:
        ndp = defaultdict(int)
        for state in dp:
            p = dp[state]
            l, r = state
            # 왼발을 움직인 경우
            if not ndp[(c, r)]:
                ndp[(c, r)] = p + power(l, c)
            else:
                ndp[(c, r)] = min(ndp[(c, r)], p + power(l, c))

            # 오른발을 움직인 경우
            if not ndp[(l, c)]:
                ndp[(l, c)] = p + power(r, c)
            else:
                ndp[(l, c)] = min(ndp[(l, c)], p + power(r, c))
        dp = ndp

    # 모든 발판을 밟았을 때 들어간 힘의 최솟값
    return min(dp.values())


# 기존 발판 - 이동할 발판이 주어졌을 때 들어가는 힘의 계산
def power(src, dst):
    if src == 0:
        return 2

    if src == dst:
        return 1

    if abs(src-dst) == 2:
        return 4
    else:
        return 3
