import sys

input = sys.stdin.readline


# 2110 공유기 설치
# n개의 수직선상의 좌표중 c개를 골랐을때 가장 인접한 두 좌표 사이의 거리의 최댓값을 구하는 문제
# 가장 가까운 두 공유기의 인접거리 최댓값을 이분탐색으로 찾아낸다
# 두 공유기의 인접거리 최솟값은 1이며
# 최댓값은 첫 번재 집부터 마지막 집 까지의 거리를 c로 나눈 값을 올림한 것 보다 작거나 같다
def sol2110():
    n, c, *house = map(int, sys.stdin.read().split())
    house.sort()
    s, e = 1, (house[-1] - house[0]) // c + 1
    while s <= e:
        m = (s + e) // 2
        cnt, prev = 1, house[0] + m
        for h in house[1:]:
            if h >= prev:
                cnt, prev = cnt+1, h + m
        s, e = (m+1, e) if cnt >= c else (s, m-1)
    print(e)
