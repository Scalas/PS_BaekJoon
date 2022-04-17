import sys

input = sys.stdin.readline


# 14476 최대공약수 하나뺴기
# n개의 정수가 주어졌을 때, 주어진 정수중 하나를 빼고 구한 최대공약수의 최댓값을 구하는 문제
# 단, 정수를 빼고 구한 최대공약수가 뺀 정수의 약수여서는 안된다.
def sol14476():
    n = int(input())
    seq = list(map(int, input().split()))

    # 주어진 수의 왼쪽, 오른쪽으로부터의 최대공약수를 누적으로 구함
    left, right = [seq[0]], [seq[-1]]
    for i in range(1, n):
        left.append(gcd(left[-1], seq[i]))
        right.append(gcd(right[-1], seq[n-1-i]))

    # 조건을 만족하는 최대약수의 최댓값과 뺀 정수를 구함
    answer = [-1, 0]
    for i in range(n):
        cur = seq[i]
        gc = left[i-1] if i == n-1 else right[n-2-i] if i == 0 else gcd(left[i-1], right[n-2-i])
        if cur % gc and answer[0] < gc:
            answer = [gc, cur]

    return -1 if answer[0] < 0 else ' '.join(map(str, answer))


# 유클리드 호제법을 사용한 두 수의 최대공약수를 구하는 함수
def gcd(u, v):
    if u < v:
        u, v = v, u
    while u % v:
        u, v = v, u % v
    return v
