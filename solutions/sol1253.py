import sys

input = sys.stdin.readline


# 1253 좋다
# n개의 수 중 어떤 수를 다른 두 수의 합으로 나타낼 수 있는 것의 갯수를 구하는 문제
def sol1253():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    answer = 0

    for i in range(n):
        target = nums[i]

        # target을 만들기 위해 더할 두 수를 투포인터로 구함
        # target을 사용하지 않도록 처리하는 것에 주의
        s, e = 0, n - 1
        if i == 0:
            s += 1
        elif i == n - 1:
            e -= 1
        while s < e:
            if s == i:
                s += 1
                continue
            if e == i:
                e -= 1
                continue
            total = nums[s] + nums[e]
            if total < target:
                s += 1
            elif total > target:
                e -= 1
            else:
                answer += 1
                break
    return answer
