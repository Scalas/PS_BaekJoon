import sys

input = sys.stdin.readline


# 17951 흩날리는 시험지 속에서 내 평점이 느껴진거야
# n개의 시험지의 맞은 문제 수가 주어지고
# 연속된 시험지들을 그룹지어 k개의 그룹을 만들었을 때
# 각 그룹의 맞은 문제 수의 합들 중 최솟값의 최댓값을 구하는 문제
def sol17951():
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))

    def check(min_score):
        nonlocal k
        total = 0
        group_count = 0
        for score in scores:
            if total + score < min_score:
                total += score
            else:
                group_count += 1
                total = 0

        return group_count >= k
    
    # parametric search로 그룹별 맞은 갯수의 최솟값으로 가능한 최대치를 탐색
    s, e = 0, 20 * n
    answer = e
    while s <= e:
        mid = (s + e) // 2
        if check(mid):
            answer = mid
            s = mid + 1
        else:
            e = mid - 1

    return answer
