import sys
from bisect import bisect_left

input = sys.stdin.readline


# 2550 전구
# 전구를 켜기위한 스위치의 번호와 전구의 번호가 위치순으로 주어지고
# 스위치는 자신과 번호가 같은 전구를 켤 수 있으며 눌린 스위치들과 연결된 전구들간의
# 전선들이 교차할 경우 전구는 켜지지 않는다고 할때, 최대한 많은 전구를 켜기 위해
# 눌러야할 스위치의 갯수와 스위치들의 번호를 구하는 문제(단, 스위치들의 번호는 오름차순 정렬하여 출력한다)
def sol2550():
    n = int(input())
    # 스위치
    switch = list(map(int, input().split()))

    # 전구
    bulb = list(map(int, input().split()))

    # 스위치가 연결된 전구의 순번
    connect = [0] * (n + 1)
    for i in range(1, n+1):
        connect[bulb[i-1]] = i

    # 가장 많은 전구를 켤 수 있는 경우를 탐색(lis)
    f, *seq = [(connect[s], s) for s in switch]
    lis = [f[0]]
    lis_s = [f[1]]
    trace = [0] * (n + 1)
    for num, s in seq:
        if num > lis[-1]:
            trace[s] = lis_s[-1]
            lis.append(num)
            lis_s.append(s)
        else:
            idx = bisect_left(lis, num)
            lis[idx] = num
            lis_s[idx] = s
            if idx > 0:
                trace[s] = lis_s[idx-1]

    # trace로 lis_s 리스트를 역추적하여 실제로 눌린 스위치들의 번호를 구함
    lis_real = [lis_s[-1]]
    while trace[lis_real[-1]]:
        lis_real.append(trace[lis_real[-1]])

    # 스위치 번호를 오름차순 정렬
    lis_real.sort()

    # 켤 수 있는 전구의 최대 갯수와 함께 출력
    return '\n'.join([str(len(lis)), ' '.join(map(str, lis_real))])
