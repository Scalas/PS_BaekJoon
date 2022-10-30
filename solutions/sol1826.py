import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 1826 연료 채우기
# 1 만큼의 거리를 갈 때마다 1의 연료를 소모하고
# n개의 주유소의 위치와 주유소에서 얻을 수 있는 연료의 양이 주어질 때
# 시작지점(0) 에서 마을로 가는 사이에 주유소에 들르는 횟수를 최소화하여 마을로 가기 위해
# 들러야할 주유소의 최소 갯수를 구하는 문제
def sol1826():
    n = int(input())
    station = [list(map(int, input().split())) for _ in range(n)]
    station.sort()
    cur_pos = 0
    target_pos, cur_gas = map(int, input().split())

    # 매 순간 갈 수 있는 모든 주유소를 heap에 추가하고
    # 그중 가장 많은 연료를 얻을 수 있는 곳을 다음 목적지로 한다
    # 얻은 연료의 총량이 목적지까지의 거리 이상이 되면 더이상 주유소를 경유할 필요가 없다.
    nxt = []
    idx = 0
    answer = 0
    while cur_gas < target_pos:
        while idx < n:
            nxt_pos, earn_gas = station[idx]
            if nxt_pos <= cur_gas:
                heappush(nxt, (-earn_gas, nxt_pos))
                idx += 1
            else:
                break
        if not nxt:
            return -1
        max_earn, nxt_pos = heappop(nxt)
        cur_pos, cur_gas = nxt_pos, cur_gas - max_earn
        answer += 1

    return answer
