import sys

input = sys.stdin.readline


# 13398 연속합 2
# n개의 정수로 이루어진 수열에서 가장 큰 연속구간의 합을 구하는문제
# 단, 1개의 수를 수열에서 제거할 수 있으며 숫자는 하나이상 선택해야한다
def sol13398():
    n = int(input())
    seq = list(map(int, input().split()))

    # 수열 최댓값
    mv = max(seq)

    # 수열의 모든 값이 음수라면 더할수록 작아지기 때문에
    # 수열 중 가장 큰 수 하나의 값이 답이된다.
    if mv < 0:
        return mv

    # a: 수열에서 하나의 수를 빼지 않은 경우의 최댓값 / b: 수열에서 하나의 수를 뺀 경우의 최댓값
    a, b = seq[0], 0

    # 답은 아무리 작아도 수열의 최댓값 이상
    answer = mv
    for i in range(1, n):
        # a: 2가지 경우의수
        #   1. 이전에 수를 빼지 않은 경우의 최댓값에 이번 숫자를 더한다.
        #   2. 이번 숫자를 구간의 시작으로 한다.
        #
        # b: 3가지 경우의 수
        #   1. 이전에 수를 빼지 않은 경우의 최댓값을 가져온다.
        #   2. 이전에 수를 뺀 경우의 최댓값에 이번 숫자를 더한다.
        #   3. 이번 숫자를 연속구간의 시작으로 하고 이번 숫자를 수열에서 뺀다.
        a, b = max(a + seq[i], seq[i]), max(a, b+seq[i], 0)
        answer = max(answer, a, b)

    return answer
