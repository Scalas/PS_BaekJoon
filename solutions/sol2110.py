import sys

input = sys.stdin.readline


# 2110 공유기 설치
# n개의 수직선상의 좌표중 c개를 골랐을때 가장 인접한 두 좌표 사이의 거리의 최댓값을 구하는 문제
# 이분탐색으로 해결가능
def sol2110():
    n, c = map(int, input().split())
    house = [int(input()) for _ in range(n)]
    house.sort()

    s, e = min([house[i + 1] - house[i] for i in range(n - 1)]), house[-1] // c
    answer = 0
    while (s <= e):
        mid = (s + e) // 2
        if check(house, mid, c):
            answer = mid
            s = mid + 1
        else:
            e = mid - 1
    print(answer)


def check(house, d, c):
    cnt = 1
    pre = house[0]
    for i in range(1, len(house)):
        if (house[i] - pre >= d):
            cnt += 1
            pre = house[i]
    return cnt >= c
