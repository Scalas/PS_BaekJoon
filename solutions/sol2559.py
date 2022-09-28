import sys

input = sys.stdin.readline


# 2559 수열
# 연속한 k 일 간의 부분수열의 합의 최댓값을 구하는 문제
def sol2559():
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))

    s, e = 0, k
    total = sum(seq[:k])
    max_total = total
    while e < n:
        total += seq[e]
        total -= seq[s]
        s += 1
        e += 1
        max_total = max(max_total, total)

    return max_total
