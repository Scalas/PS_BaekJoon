import sys

input = sys.stdin.readline


# 2670 연속부분최대곱
# 실수로 이루어진 수열에서 연속하는 구간의 곱이 최대가 되는 경우를 구하는 문제
def sol2670():
    n = int(input())
    seq = [float(input()) for _ in range(n)]

    # i번째 칸을 포함하는 i번째 칸까지의 연속부분최대곱은
    # 이전 칸의 연속부분최대곱에 현재 칸의 값을 곱한 값과
    # 현재 칸의 값중 최댓값이 된다
    for i in range(1, n):
        seq[i] = max(seq[i], seq[i-1]*seq[i])

    # 각 칸의 연속부분최대곱중 최댓값 반환
    return '%.3f' % max(seq)
