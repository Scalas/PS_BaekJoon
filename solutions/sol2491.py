import sys

input = sys.stdin.readline


# 2491 수열
# 증가 혹은 감소하는 연속구간의 길이중 최댓값을 구하는 문제
def sol2491():
    n = int(input())
    f, *seq = map(int, input().split())

    # 단순히 수열의 숫자를 순차적으로 탐색하며 최장증가연속부분수열과 최장감소연속부분수열의 길이를 갱신
    ic, dc = 1, 1
    tic, tdc = 1, 1
    for num in seq:
        if num > f:
            tic += 1
            dc = max(dc, tdc)
            tdc = 1
        elif num < f:
            tdc += 1
            ic = max(ic, tic)
            tic = 1
        else:
            tdc += 1
            tic += 1
        f = num
    ic = max(ic, tic)
    dc = max(dc, tdc)

    # 둘 중 최댓값 반환
    return max(ic, dc)
