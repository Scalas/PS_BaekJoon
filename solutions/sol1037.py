import sys

input = sys.stdin.read


# 1037 약수
# 어떤 수 N의 진짜약수가 모두 주어졌을 때, N을 구하는 문제
def sol1037():
    n, *nums = map(int, input().split())

    # 가장 큰 약수와 가장 작은 약수를 곱하면 N을 구할 수 있다.
    nums.sort()
    print(nums[0] * nums[-1])
