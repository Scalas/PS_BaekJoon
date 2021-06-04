import sys
from itertools import permutations

input = sys.stdin.readline


# 14888 연산자 끼워넣기
# 숫자 사이에 연산자를 넣어 만들 수 있는 최댓값과 최솟값을 구하는 문제

# 두 수의 사이를 각각 하나의 슬롯으로 하여 슬롯당 한종류씩 연산자를 넣어보며 완전탐색으로 최대, 최소 값을 구한다
def sol14888():
    n = int(input())
    nums = list(map(int, input().split()))
    p, m, x, d = map(int, input().split())
    answer = [float('-inf'), float('inf')]
    dfs(nums, p, m, x, d, answer, nums[0], 0)
    print(*answer, sep='\n')


def dfs(nums, p, m, x, d, answer, cur, slot):
    if (slot == len(nums) - 1):
        answer[0] = max(answer[0], cur)
        answer[1] = min(answer[1], cur)
        return
    if p:
        dfs(nums, p-1, m, x, d, answer, cur+nums[slot + 1], slot + 1)
    if m:
        dfs(nums, p, m-1, x, d, answer, cur-nums[slot + 1], slot + 1)
    if x:
        dfs(nums, p, m, x-1, d, answer, cur*nums[slot + 1], slot + 1)
    if d:
        res = -(-cur//nums[slot + 1]) if cur<0 else cur//nums[slot + 1]
        dfs(nums, p, m, x, d-1, answer, res, slot + 1)


# itertools 의 permutations 클래스를 활용한 풀이
# 한종류의 연산자가 여러개 들어 있을 수 있기 때문에 완전탐색보다 많은 연산이 필요
# 집합으로 변환하여 중복을 제거하는 것으로 시간초과 없이 통과는 가능하지만 여전히 완전탐색보다 속도가 느림
def sol14888_2():
    n = int(input())
    nums = list(map(int, input().split()))
    ops = []
    for o, c in enumerate(map(int, input().split())):
        for _ in range(c):
            ops.append(o)
    min_val = float('inf')
    max_val = float('-inf')
    for case in set(permutations(ops, n-1)):
        res = nums[0]
        for idx, o in enumerate(case):
            res = calc(res, nums[idx+1], o)
        min_val = min(min_val, res)
        max_val = max(max_val, res)
    print(max_val, min_val, sep='\n')


def calc(a, b, o):
    if (o == 0):
        return a + b
    elif (o == 1):
        return a - b
    elif (o == 2):
        return a * b
    else:
        return -(-a // b) if a<0 and b>0 else a//b
