import sys
import math

input = sys.stdin.readline


# 11653 소인수분해
# 정수 n의 소인수를 모두 구하는 문제


# 제일 작은 약수를 찾아 소인수 목록에 추가하고
# 구한 소인수로 나눈 결과에 대해 다시 그 과정을 반복
def sol11653():
    n = int(input())
    if n > 1:
        answer = []
        factor(n, answer)
        print(*answer, sep='\n')


def factor(n, buf):
    if n <= 3:
        buf.append(n)
        return

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            buf.append(i)
            return factor(n // i, buf)

    buf.append(n)
    return