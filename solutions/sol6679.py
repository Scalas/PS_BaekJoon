import sys

input = sys.stdin.readline


# 6679 싱기한 네자리 숫자
# 1000 ~ 9999의 네자리 10진수 중 10진수, 12진수, 16진수로 표현했을 때
# 모든 자릿수의 합이 서로 같아지는 수를 구하는 문제
def sol6679():
    return '\n'.join(map(str, [i for i in range(2992, 10000) if check(i)]))


def check(num_10):
    o1, o2, o3 = 0, 0, 0

    num = num_10
    while num:
        o1 += (num % 10)
        num //= 10

    num = num_10
    while num:
        o2 += (num % 12)
        num //= 12

    num = num_10
    while num:
        o3 += (num % 16)
        num //= 16

    return o1 == o2 == o3
