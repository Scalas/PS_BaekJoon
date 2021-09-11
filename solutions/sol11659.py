import sys

input = sys.stdin.readline


# 11659 구간 합 구하기
# n개의 수로 이루어진 수열이 주어졌을 때
# 수열의 i부터 j까지의 수를 합한 값을 구하는 문제
# 누적합을 활용하여 구간합을 구하는 연습문제이다.
def sol11659():
    # 수열의 크기 n, 질의의 갯수 m
    n, m = map(int, input().split())

    # n개의 수로 이루어진 수열
    seq = [0, *map(int, input().split())]

    # 수열의 누적합 전처리
    for i in range(1, n + 1):
        seq[i] += seq[i - 1]

    # 각 질의에 대해 정답을 계산하여 answer 에 삽입
    answer = []
    for _ in range(m):
        i, j = map(int, input().split())
        answer.append(seq[j] - seq[i - 1])

    # 출력형식에 맞춰 정답리스트 반환환
    return '\n'.join(map(str, answer))

