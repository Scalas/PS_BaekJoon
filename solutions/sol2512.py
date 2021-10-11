import sys

input = sys.stdin.readline


# 2512 예산
# 예산의 상한치를 정하여 상한치를 각 지방의 예산에 대해 예산이 상한치를 넘지 않는다면 예산대로, 넘는다면 상한치를 배정
# 총 예산을 넘지 않으며 최대한 많은 예산을 지원하기 위한 상한치를 찾는 문제
# 이분탐색으로 간단하게 해결 가능하다
def sol2512():
    n = int(input())
    budgets = list(map(int, input().split()))
    cap = int(input())

    s, e = cap // n, max(budgets)
    while s <= e:
        mid = (s + e) // 2
        if sum([budget if budget < mid else mid for budget in budgets]) <= cap:
            s = mid + 1
        else:
            e = mid - 1
    return s - 1
