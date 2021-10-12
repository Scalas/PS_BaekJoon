import sys
from bisect import bisect_right

input = sys.stdin.read


# 2343 기타 레슨
# n 개의 강의를 순서를 지켜 m개의 같은 크기를 가진 블루레이로 합쳐야할 때
# 가능한 블루레이의 최소크기를 구하는 문제
def sol2343():
    n, m, *seq = map(int, input().split())

    # 각 강의를 담을 수는 있어야하기 때문에 적어도 가장 큰 강의보다는 커야한다
    # 강의 전체의 합보다는 작다
    s, e = max(seq), sum(seq)

    # 강의 크기의 누적합
    for i in range(n - 1):
        seq[i + 1] += seq[i]

    # 범위내에서 이분탐색
    while s <= e:
        mid = (s + e) // 2
        # 블루레이 크기가 mid 일때 m개 이하의 블루레이로 강의를 모두 담을 수 있는 경우
        if simulate(seq, mid, m):
            e = mid - 1
        # 담을 수 없는 경우
        else:
            s = mid + 1
    # 마지막으로 m개 이하의 갯수로 모든 강의를 담는데 성공한 블루레이의 크기 반환
    return e + 1


# 블루레이의 크기가 size 일 때 m개 이하의 블루레이에 강의를 모두 담을 수 있는지 검사하는 함수
def simulate(seq, size, m):
    sub = 0
    # 강의 크기의 누적합배열 seq 에서 size 보다 크거나 작은 값의 마지막 인덱스를 찾은 뒤
    # 해당 순번까지의 강의는 블루레이에 넣은 것으로 처리, sub 의 크기는 블루레이에 넣는데 성공한 강의들의 크기의 합
    for _ in range(m):
        sub = seq[bisect_right(seq, size + sub) - 1]
        if sub == seq[-1]:
            break

    # m 번 이내에 sub 가 강의 전체의 합에 도달하지 못했다면 m개 이하의 블루레이에 압축하는 것은 불가능
    return True if sub == seq[-1] else False
