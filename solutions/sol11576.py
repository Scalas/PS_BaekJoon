import sys

input = sys.stdin.read


# 11576 Base Conversion
# a 진법으로 나타낸 숫자의 각 자릿수를 공백으로 구분하여 입력받아
# b 진수로 변환하여 각 자릿수를 공백으로 구분하여 출력하는 문제
def sol11576():
    a, b, m, *digits = map(int, input().split())
    num = 0
    power = len(digits) - 1
    for d in digits:
        num += d * (a ** power)
        power -= 1

    answer = []
    while num:
        answer.append(num % b)
        num //= b
    return ' '.join(map(str, answer[::-1]))
