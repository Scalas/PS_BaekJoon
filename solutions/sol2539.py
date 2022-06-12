import sys

input = sys.stdin.readline


# 2539 모자이크
# n * m 격자공간에 색이 잘못칠해진 칸의 좌표가 주어지고
# 정사각형 크기의 색종이 k개를 밑면에 닿도록 붙여 모든 잘못 칠해진 칸을 덮으려 할 때
# 가능한 색종이의 최소 크기(한 변의 길이)를 구하는 문제
# 단, 색종이는 겹쳐서도 붙일 수 있다.
def sol2539():
    n, m = map(int, input().split())
    k = int(input())
    e = int(input())

    # 잘못 칠해 칸의 높이 최댓값과 잘못 칠해진 칸이 분포하는 구간
    h_max = 0
    w_min = 1000001
    w_max = 0

    # 잘못 칠해진 칸들의 좌표
    errors = set()
    for _ in range(e):
        u, v = map(int, input().split())
        h_max = max(h_max, u)
        w_min = min(w_min, v)
        w_max = max(w_max, v)
        errors.add(v)

    # 좌표를 오름차순으로 정렬
    errors = sorted(errors)

    # size 크기의 색종이 k개로 잘못 칠해진 칸을 모두 덮을 수 있는지 체크
    def check(size):
        last = errors[0]
        cnt = 1
        for error in errors:
            if error >= last + size:
                last = error
                cnt += 1
        if cnt <= k:
            return True
        return False

    # 색종이는 잘못 칠해진 칸의 최대 높이보다는 반드시 크거나 같아야하며
    # 잘못 칠해진 칸이 존재하는 구간의 전체 길이와 잘못 칠해진 칸의 최대 높이중 최댓값 이상부터는
    # 반드시 모든 잘못 칠해진 칸을 덮을 수 있다.
    s, e = h_max, max(h_max, w_max - w_min + 1)

    # 이분탐색으로 모든 잘못 칠해진 칸을 덮을 수 있는 최소 크기를 탐색
    while s < e:
        mid = (s + e) // 2
        if check(mid):
            e = mid
        else:
            s = mid + 1

    return e
