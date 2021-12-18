import sys

input = sys.stdin.readline
INF = 36 * 16


# 1102 발전소
# n개의 발전소에 대해 켜져있는 i 발전소로 꺼져있는 j 발전소를 켜기위해 드는 비용과
# 발전소의 on/off 상태, 켜져있어야할 발전소의 최소갯수가 주어졌을 때
# 켜져있어야할 발전소의 최소갯수를 만족시키기 위해 필요한 최소비용을 구하는문제
def sol1102():
    # 발전소의 갯수
    n = int(input())

    # cost[i][j] 는 발전소 i로 발전소 j를 고치기 위해 드는 비용
    cost = [list(map(int, input().split())) for _ in range(n)]

    bit = [1 << i for i in range(n)]

    # 발전소의 상태가 state 이고 켜야할 발전소의 갯수가 cnt 개일 때
    # 남은 갯수만큼 발전소를 켜는데 들어가는 최소비용을 반환
    def dfs(state, cnt):
        # 더이상 켜야할 발전소가 없다면 0 반환
        if not cnt:
            return 0

        # 아직 현재 발전소 상태에서 cnt개만큼 켜야할 경우의 최소비용이 계산되지 않은 경우
        if dp.get((state, cnt), -1) < 0:
            res = INF

            # 다음으로 꺼야할 발전소를 선택
            for i in range(n):
                # 꺼진 발전소일 경우
                if not (state & bit[i]):
                    # 켜져있는 발전소중 해당 발전소를 켜기위한 비용이 가장 적은 것을 탐색
                    minc = min([cost[j][i] for j in range(n) if state & bit[j]])

                    # (현재 발전소를 켜는 비용) + (나머지 cnt-1 개의 발전소를 켜는데 드는 비용)으로 최소비용을 갱신
                    res = min(res, dfs(state + bit[i], cnt - 1) + minc)
            dp[(state, cnt)] = res

        # 현재 발전소 상태에서 cnt개의 발전소를 켜기위한 최소비용 반환
        return dp[(state, cnt)]

    # 각 발전소의 초기상태를 비트마스크로 저장
    # 켜진 발전소의 갯수를 카운트
    state = 0
    state_str = input().rstrip()
    on = 0
    for i in range(n):
        if state_str[i] == 'Y':
            state += (1 << i)
            on += 1

    # 켜져있어야하는 발전소 갯수
    k = int(input())

    # 켜져있어야하는 발전소의 수가 1개 이상이고 모든 발전소가 꺼져있을 경우 불가능
    if k and not on:
        return -1

    # 앞으로 켜야할 발전소의 갯수
    cnt = k - on

    # 이미 조건을 만족하고있을 경우
    if cnt <= 0:
        return 0

    # 이미 계산한 상태를 저장할 딕셔너리
    dp = dict()

    # cnt개의 발전소를 켜기 위한 최소비용을 계산하여 반환
    return dfs(state, cnt)
