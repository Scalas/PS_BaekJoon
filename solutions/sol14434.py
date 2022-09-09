import sys
from bisect import bisect_right

input = sys.stdin.readline


# 14434 놀이기구 1
# n명의 아이들의 키가 처음에 0으로 시작하여 매일 누군가 한명의 키가 1씩 늘어난다.
# m개의 놀이기구는 각각 키 제한이 있고 2인승이며 타는 두 사람의 키의 합이 키 제한을 넘겨야만 탑승이 가능하다.
# k일 동안 매일 키가 자란 아이의 번호가 주어지고
# k일동안 매일 놀이기구에 타려는 두 아이의 번호와 타려는 놀이기구의 번호가 q개 주어졌을 때
# 각 일마다 놀이기구에 타는데 성공한 아이의 수를 구하는 문제
def sol14434():
    n, m, k, q = map(int, input().split())
    rides = list(map(int, input().split()))

    # 각 아이의 키가 자란 일수를 리스트로 관리
    grow = [[] for _ in range(n)]
    grow_per_day = list(map(int, input().split()))
    for i in range(k):
        grow[grow_per_day[i] - 1].append(i)

    answer = [0] * k
    for _ in range(q):
        u, v, w = map(int, input().split())

        # 끝까지 탈 수 없다면 continue
        if len(grow[u - 1]) + len(grow[v - 1]) < rides[w - 1]:
            continue

        # 놀이기구를 타는데 처음으로 성공하는 날을 이분탐색으로 구함
        s, e = 0, k - 1
        while s < e:
            mid = (s + e) // 2
            # 현재 일수(mid) 이하인 아이의 키가 자란 일수의 갯수를 이분탐색으로 구하면 그 날 아이의 키를 구할 수 있음
            if bisect_right(grow[u - 1], mid) + bisect_right(grow[v - 1], mid) < rides[w - 1]:
                s = mid + 1
            else:
                e = mid
        answer[e] += 1

    # 누적합으로 매일 놀이기구를 타는데 성공한 아이의 수를 구함
    for i in range(k - 1):
        answer[i + 1] += answer[i]

    return '\n'.join(map(str, answer))
