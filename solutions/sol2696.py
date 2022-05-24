import sys
from heapq import heappush, heappop
from math import ceil

input = sys.stdin.readline


# 2696 중앙값 구하기
# n개의 숫자를 차례대로 읽으며 홀수개의 숫자를 읽을 때마다
# 지금까지 읽은 수 중 중앙값을 구하는 문제
def sol2696():
    answer = []
    for _ in range(int(input())):
        n = int(input())
        mediums = []
        minh, maxh = [], []
        nums = []
        for _ in range(ceil(n / 10)):
            for num in map(int, input().split()):
                nums.append(num)

        answer.append(str(n // 2 + 1))
        for i in range(n):
            if minh and nums[i] < minh[0]:
                heappush(maxh, -nums[i])
            else:
                heappush(minh, nums[i])
            if not i % 2:
                while True:
                    if len(minh) - len(maxh) > 1:
                        heappush(maxh, -heappop(minh))
                    elif len(minh) - len(maxh) < 1:
                        heappush(minh, -heappop(maxh))
                    else:
                        break
                mediums.append(minh[0])
                if len(mediums) == 10:
                    answer.append(' '.join(map(str, mediums)))
                    mediums = []
        if mediums:
            answer.append(' '.join(map(str, mediums)))

    return '\n'.join(answer)
