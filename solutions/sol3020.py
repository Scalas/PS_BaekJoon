import sys
from bisect import bisect_right

input = sys.stdin.read


# 3020 개똥벌레
# 누적합의 응용문제
# 결국 각 구간에 몇개의 벽이 있는지 알고있다면 쉽게 해결 가능한 문제이다
# 구간의 누적을 누적합을 활용하여 한번에 구하면 O(N+H) 의 시간복잡도로
# 각 구간의 장애물 갯수를 구할 수 있으며 이를 오름차순 정렬하고 배열의
# 첫 번째 값(부숴야할 장애물의 최소갯수)의 upper bound 를 이분탐색으로 구하면
# O(logH) 의 시간복잡도로 구간의 갯수를 구할 수 있다.
def sol3020():
    n, h, *obs = map(int, input().split())

    obs_h = [0] * (h+1)
    for i in range(n):
        if i % 2:
            obs_h[h] += -1
            obs_h[h - obs[i]] += 1
        else:
            obs_h[0] += 1
            obs_h[obs[i]] += -1
    for i in range(h):
        obs_h[i + 1] += obs_h[i]

    obs_h.sort()
    return '%d %d' % (obs_h[1], bisect_right(obs_h, obs_h[1]) - 1)
