# 2981 검문
# n 개의 수를 m으로 나눠 그 나머지가 모두 같게 하는 m을 모두 구하는 문제
# n개의 수를 정렬한 뒤 인접한 수 끼리의 차들의 최대 공약수를 구하고, 그 최대 공약수의 약수를 구하는 방식으로 접근해야함
# A1 = a1 * m + r,  A2 = a2 * m + r
# A2 - A1 = (a2 - a1) * m
# 약수를 구할때는 최대공약수의 제곱근까지만 탐색, 나눈 m값과 몫이 모두 약수가 된다
# 1을 포함하지 않기때문에 최대공약수 자체도 따로 추가해줘야한다

import sys
import math

input = sys.stdin.readline


def gcd(a, b):
    r = a % b
    if (r == 0):
        return b
    else:
        return gcd(b, r)


def sol2981():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    g = nums[1]-nums[0]
    if(n>2):
        diff = [nums[i + 1] - nums[i] for i in range(n - 1)]
        g = gcd(diff[0], diff[1])
        for i in range(2, n - 1):
            g = gcd(g, diff[i])

    answer = []
    for m in range(2, int(math.sqrt(g))+1):
        if (g % m == 0):
            answer.append(m)
            if(m != g//m):
                answer.append(g//m)

    answer.append(g)
    answer.sort()
    print(*answer)

