import sys

input = sys.stdin.readline


# 2613 숫자구슬
# n개의 순서대로 주어진 숫자구슬을 m개의 그룹으로 나누었을 때
# 각 그룹의 숫자의 합중 최댓값이 최소가 되도록 그룹은 분할하고
# 그 때, 각 그룹의 합의 최댓값과 그룹을 구성하는 구슬의 갯수를 순서대로 구하는 문제
# 단, 그룹을 이루는 구슬의 갯수는 최소 1개 이상
def sol2613():
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))

    # 그룹의 합의 최댓값은 아무리 작아도 seq의 최댓값이상이며
    # 아무리 커도 seq 전체의 합 이하
    s, e = max(seq), sum(seq)
    group = None
    while s < e:
        mid = (s + e) // 2
        # mid 가 그룹의 합의 최댓값이라고 할 때 m개의 그룹으로 분할 시도
        check = grouping(seq, mid, m)

        # 구슬을 m개의 그룹으로 나눌 수 있다면 group 에 분할 결과를 저장하고 e를 mid 로 하여 재탐색
        if check:
            e = mid
            group = check
        # 나눌 수 없다면 s를 mid+1로 하여 재탐색
        else:
            s = mid+1

    return '\n'.join([str(e), ' '.join(map(str, group))])


# 그룹 분할
def grouping(seq, mid, m):
    gs, gc = 0, 0
    group = []
    # 구슬을 순차적으로 더해나가며 합이 mid를 넘지 않는 그룹으로 묶는다
    for num in seq:
        # 그룹에 현재 구슬을 더하면 mid를 넘는다면 그룹을 이루는 구슬 갯수를 group에 append
        # 새로운 그룹에는 현재 구슬만이 들어있는 상태로 초기화
        if gs + num > mid:
            group.append(gc)
            gs, gc = num, 1

        # 현재 구슬을 더해도 mid를 넘지 않는다면 그룹에 현재 구슬을 추가
        else:
            gs += num
            gc += 1
    # group에 추가되지 않은 그룹이 있다면 추가
    if gs:
        group.append(gc)

    # 그룹의 갯수가 m개를 초과할 경우 m개의 그룹으로 나눌 수 없음
    if len(group) > m:
        return

    # 그룹의 갯수가 m 개보다 작을 경우 m개가 될 때까지 2개 이상의 구슬로 이뤄진 그룹을 분할
    while len(group) < m:
        for i in range(len(group)):
            if group[i] > 1:
                group.insert(i, 1)
                group[i+1] -= 1
                break

    # 만들어진 m개의 그룹을 구성하는 구슬의 갯수 리스트를 반환
    return group
