import sys
import math

input = sys.stdin.read


# 1978 소수 찾기
# 단순히 2부터 n까지 모두 나누어보는 것으로 소수를 찾는 문제

# 조금이라도 연산을 줄이기 위해 sqrt(n) 까지만 계산
def sol1978():
    n, *nums = map(int, input().split())
    answer = 0
    for num in nums:
        if isPrime(num):
            answer += 1
    print(answer)


def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True
