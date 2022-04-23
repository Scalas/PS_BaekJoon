import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline


# 1933 스카이라인
# n개의 직사각형 건물의 시작 x좌표, 끝 x좌표, 높이가 주어졌을 때
# 건물 전체의 윤곽을 합친 후 윤곽의 높이가 달라지는 x좌표와 그 때의 윤곽의 높이를 구하는 문제
def sol1933():
    n = int(input())

    # height[i] 는 i번 건물의 높이
    height = dict()

    # start_building[i] 는 위치 i에서 시작되는 건물
    # end_building[i] 는 위치 i에서 끝나는 건물
    start_buildings = defaultdict(list)
    end_buildings = defaultdict(list)

    # 변화가 발생할 가능성이 있는 x좌표
    x_pos = set()

    for i in range(n):
        u, v, w = map(int, input().split())
        height[i] = v
        start_buildings[u].append(i)
        end_buildings[w].append(i)
        x_pos.add(u)
        x_pos.add(w)

    # 변화가 발생한 x좌표와 그 시점의 높이
    skyline = []

    # 현재 존재하는 빌딩들의 높이
    buildings = []

    # 빌딩의 제거여부
    deleted = [False] * n

    # 변화가 발생할 수 있는 모든 x좌표를 순회
    for x in sorted(x_pos):
        # 이 시점에서 시작되는 빌딩을 buildings에 추가
        # 끝나는 빌딩을 제거
        for building in start_buildings[x]:
            heappush(buildings, (-height[building], building))
        for building in end_buildings[x]:
            deleted[building] = True

        # 제거된 빌딩을 heappop
        while buildings and deleted[buildings[0][1]]:
            heappop(buildings)

        # 빌딩의 현재높이는 buildings의 높이중 최댓값
        # 빌딩이 존재하지 않을경우 0
        cur_height = -buildings[0][0] if buildings else 0

        # 이전과 높이가 달라졌다면 skyline에 좌표와 높이 추가
        if not skyline or skyline[-1] != cur_height:
            skyline.append(x)
            skyline.append(cur_height)

    return ' '.join(map(str, skyline))
