import sys

input = sys.stdin.readline


# 6209 제자리 멀리뛰기
# 시작위치로부터 도착위치까지의 거리 d와
# 돌섬의 갯수 n과 그중 제거 가능한 돌섬의 갯수 m이 주어지고
# n개의 돌섬의 시작 위치로부터의 거리가 주어졌을 때
# 돌섬을 m개 제거했을 때의 시작위치로부터 도착 위치까지의 간격중 최솟값의 최댓값을 구하는 문제
def sol6209():
    d, n, m = map(int, input().split())

    # 돌섬을 위치순으로 정렬
    stones = [int(input()) for _ in range(n)]
    stones.sort()

    # 돌섬간 거리를 mind 이상으로 유지하며
    # m개를 넘는 돌섬을 제거하지 않고 도착위치에 도달 가능한지 확인
    def check(mind):
        pre = 0
        cnt = m
        for stone in stones:
            # 이전 돌섬과의 거리가 mind보다 작다면 현재 돌섬을 제거
            # 돌섬을 제거할 수 없다면 도달 불가능
            if stone - pre < mind:
                if not cnt:
                    return False
                cnt -= 1
                continue

            # 이전 돌섬의 위치를 갱신
            pre = stone

        # 마지막 돌섬과 도착 위치간의 거리가 mind 미만이고 돌섬을 제거할 수 없다면 도달 불가능
        if d - pre < mind and not cnt:
            return False

        return True

    # 가능한 최소거리의 최댓값을 탐색
    s, e = 1, d
    while s < e:
        mid = (s + e + 1) // 2
        if check(mid):
            s = mid
        else:
            e = mid - 1

    return s
