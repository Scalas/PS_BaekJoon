import sys

input = sys.stdin.read


# 10773 제로
# 스택을 활용하여 풀 수 있는 간단한 문제
def sol10773():
    k, *nums = map(int, input().split())
    stack = []
    for num in nums:
        if num != 0:
            stack.append(num)
        else:
            stack.pop()
    print(sum(stack))
