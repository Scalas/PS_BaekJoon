import sys
from collections import defaultdict

input = sys.stdin.readline


# 2592 대표값
# 주어진 수열의 평균과 최빈값을 구하는 문제
def sol2592():
    count = defaultdict(int)
    total = 0
    for _ in range(10):
        num = int(input())
        total += num
        count[num] += 1
    return '\n'.join(map(str, [total//10, max(count.keys(), key=lambda x:count[x])]))
