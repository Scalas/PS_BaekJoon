import sys

input = sys.stdin.read


def sol1037():
    n, *nums = map(int, input().split())
    nums.sort()
    print(nums[0] * nums[-1])
