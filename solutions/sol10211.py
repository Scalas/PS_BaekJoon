import sys

input = sys.stdin.readline


# 10211 Maximum Subarray
# 부분연속수열의 합의 최댓값을 구하는 문제
def sol10211():
    answer = []
    for _ in range(int(input())):
        n = int(input())
        x = list(map(int, input().split()))
        res = x[0]
        for i in range(1, n):
            x[i] = max(x[i]+x[i-1], x[i])
            res = max(res, x[i])
        answer.append(res)
    return '\n'.join(map(str, answer))
