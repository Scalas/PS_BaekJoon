import sys

input = sys.stdin.read


# 3079 입국심사
# 심사대의 갯수와 심사받아야할 인원수, 각 심사대의 처리시간이 주어졌을 때
# 모든 심사를 마치는데 걸리는 시간의 최소값을 구하는 문제
def sol3079():
    # 심사대의 갯수와 심사받아야할 인원수, 각 심사대의 처리시간
    n, m, *t = map(int, input().split())

    # 가장 처리속도가 빠른 심사대만 n개일 경우, 가장 처리속도가 느린 심사대만 m개일 경우로
    # 이분탐색의 최소 최대 범위를 좁힌 후 이분탐색 실행
    s, e = m // n * min(t), m // n * max(t)
    while s <= e:
        mid = (s + e) // 2
        # 심사시간이 mid 일 때 심사대가 처리할 수 있는 최대 인원수
        check = 0
        for tk in t:
            check += mid//tk

        # m명의 인원을 처리할 수 없는 경우 시간의 범위를 상향조정하여 재탐색
        if check < m:
            s = mid + 1
        # 처리할 수 있는 경우 시간의 범위를 하향조정하여 재탐색
        else:
            e = mid - 1

    # 마지막으로 처리에 성공한 시간을 반환
    return e+1
