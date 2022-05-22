import sys
from collections import defaultdict

input = sys.stdin.readline
INF = 10 ** 9


# 15976 XCorr
# 두 수열 s1, s2에 대해 Xcorr(k) 는 sum([s1[i] * s2[i+k] for i in range(n-1)]) 이다.
# 두 수열 s1, s2와 구간 a, b(a <= b)가 주어졌을 때 Xcorr[a] + Xcorr[a+1] + ... + Xcorr[b-1] + Xcorr[b]을 구하는 문제
def sol15976():
    # 수열 s1, s2의 누적합(0인 구간을 제외한)
    s1 = defaultdict(int)
    s2 = defaultdict(int)
    for _ in range(int(input())):
        u, v = map(int, input().split())
        s2[u] += v
    for _ in range(int(input())):
        u, v = map(int, input().split())
        s1[u] += v

    # a, b
    a = int(input())
    b = int(input())

    # s1의 각 요소에 곱해져야할 수를 구하여 곱하고 그 값을 answer에 합산
    answer = 0

    # 쿼리 저장
    query = []

    s1k = list(s1.keys())
    s2k = list(s2.keys())

    # 음수 구간
    if a < 0:
        tb = min(b, -1)
        for i in s1k:
            min_bound = i - tb
            max_bound = i - a
            s2[min_bound-1] += 0
            s2[max_bound] += 0
            query.append((s1[i], 0, min_bound, max_bound))

    # 양수 구간
    if b >= 0:
        ta = max(0, a)
        for i in s2k:
            min_bound = i + ta
            max_bound = i + b
            s1[min_bound-1] += 0
            s1[max_bound] += 0
            query.append((s2[i], 1, min_bound, max_bound))

    # s1, s2의 인덱스값
    s1k, s2k = sorted(s1.keys()), sorted(s2.keys())

    # s1, s2의 누적합을 구함
    for i in range(len(s1k)-1):
        s1[s1k[i+1]] += s1[s1k[i]]
    for i in range(len(s2k)-1):
        s2[s2k[i+1]] += s2[s2k[i]]

    for cur, t, min_bound, max_bound in query:
        if t:
            answer += (cur * (s1[max_bound] - s1[min_bound - 1]))
        else:
            answer += (cur * (s2[max_bound] - s2[min_bound - 1]))

    return answer
