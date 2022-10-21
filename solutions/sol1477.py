import sys
from math import ceil

input = sys.stdin.readline


# 1477 휴게소 세우기
# 0 ~ l 까지의 거리 사이에 n 개의 휴게소가 주어지고
# m개의 휴게소를 추가로 세웠을 때 휴게소간 간격의 최댓값의 최솟값을 구하는 문제
def sol1477():
    n, m, l = map(int, input().split())
    rest = [0, *map(int, input().split()), l]
    rest.sort()
    section = []
    for i in range(n + 1):
        section.append(rest[i + 1] - rest[i])
    section.sort(reverse=True)

    # 휴게소간 간격의 최댓값이 limit을 넘지 않도록 쪼갤 수 있는지 확인
    def check(limit):
        count = m
        for s in section:
            if s <= limit:
                break
            need = ceil(s / limit) - 1
            if need > count:
                return False
            count -= need
        return True

    # 이분탐색으로 m개의 휴게소를 세워 얻을 수 있는 휴게소 간격의 최댓값의 최솟값을 구함
    s, e = 1, section[0]
    while s < e:
        mid = (s + e) // 2
        if check(mid):
            e = mid
        else:
            s = mid + 1
    return e
