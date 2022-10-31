import sys

input = sys.stdin.readline


# 13397 구간 나누기 2
# n개의 수로 이루어진 배열을 m개의 연속구간으로 나누고
# 각 구간의 최댓값 - 최솟값 중 최댓값이 최솟값이 되는 케이스를 구하는 문제
def sol13397():
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))
    
    # 최댓값 - 최솟값의 최댓값이 max_score를 넘지 않도록 m개의 그룹을 나눌 수 있는지 확인
    def check(max_score):
        min_v, max_v = seq[0], seq[0]
        group_count = 1
        for num in seq:
            min_v = min(min_v, num)
            max_v = max(max_v, num)
            if max_v - min_v > max_score:
                min_v, max_v = num, num
                group_count += 1
        return group_count <= m

    # 이분탐색으로 가능한 max_score의 최솟값을 구함
    s, e = 0, max(seq) - min(seq)
    while s < e:
        mid = (s + e) // 2
        if check(mid):
            e = mid
        else:
            s = mid + 1

    return e
