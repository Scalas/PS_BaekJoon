import sys

input = sys.stdin.readline


# 1094 막대기
# 64cm의 막대를 반으로 나누거나 반을 버려가며 합이 x 길이가 되도록 했을 때
# 막대의 갯수를 구하는 문제
# 이진법으로 나타냈을 때 1의 갯수를 구하면 된다.
def sol1094():
    x = int(input())
    answer = 0
    while x:
        answer += (x % 2)
        x //= 2
    return answer
