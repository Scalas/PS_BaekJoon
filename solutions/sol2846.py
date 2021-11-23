import sys

input = sys.stdin.read


# 2846 오르막길
# 증가하는 부분연속수열의 최댓값 - 최솟값 의 최댓값을 구하는 문제
def sol2846():
    n, *seq = map(int, input().split())
    answer = 0
    tmp = seq[0]
    for i in range(1, n):
        if seq[i] <= seq[i-1]:
            answer = max(answer, seq[i-1]-tmp)
            tmp = seq[i]

    return max(answer, seq[-1] - tmp)
