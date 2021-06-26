import sys

input = sys.stdin.readline


# 10844 쉬운 계단 수
# 인접한 자릿수의 차가 모두 1인 n자리 수의 갯수를 구하는 문제
# n자리 계단 수를 만들려면 n-1자리 계단 수의 뒤에 각각 마지막 자릿수보다 1 작은 수, 1 큰 수를 붙여야한다
# 마지막 자릿수가 1에서 8까지인 계단 수는 두개의 계단 수를 만들어내지만
# 마지막 자릿수가 0, 9인 계단 수는 각각 1, 8인 계단 수만을 만들어낸다
def sol10844():
    n = int(input())
    mod = 1000000000
    count = [1] * 10
    count[0] = 0
    for i in range(1, n):
        tmp = [0] * 10
        tmp[1] = count[0]
        tmp[8] = count[9]
        for j in range(1, 9):
            tmp[j - 1] = (tmp[j - 1] + count[j]) % mod
            tmp[j + 1] = (tmp[j + 1] + count[j]) % mod
        count = tmp

    print(sum(count) % mod)
