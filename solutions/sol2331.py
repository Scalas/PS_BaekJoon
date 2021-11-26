import sys

input = sys.stdin.readline


# 2331 반복수열
# a 부터 시작하여 각 자릿수의 p제곱을 더한 수가 다음수가 되는 수열에서
# 반복구간을 제외한 수열의 길이를 구하는 문제
# 처음 중복된 수가 나타난 인덱스를 구하여 해결
def sol2331():
    a, p = map(int, input().split())
    nums = {}
    idx = 0
    while a not in nums:
        nums[a] = idx
        idx += 1
        tmp = 0
        while a:
            tmp += (a % 10) ** p
            a //= 10
        a = tmp
    return nums[a]
