import sys
import re
from collections import deque

input = sys.stdin.readline


# 19591 독특한 계산기
# 1. 수식에서 맨 앞의 연산자, 또는 맨 뒤의 연산자 먼저 계산한다. 단, 음수의 부호는 연산자로 취급하지 않는다.
# 2. 곱셈, 나눗셈을 덧셈, 뺄셈보다 더 먼저 계산한다.
# 3. 연산자의 우선순위가 같다면 해당 연산자를 계산했을 때 결과가 큰 것부터 계산한다.
# 4. 계산했을 때 결과 값 또한 같다면 앞에 것을 먼저 계산한다.
# 위 규칙에 따라 주어진 수식을 계산한 결과를 구하는 문제
def sol19591():
    # 연산자 우선순위
    priority = {'+': 0, '-': 0, '*': 1, '/': 1}

    # 주어진 수식
    input_str = input().rstrip()

    # 숫자 파싱 및 첫 숫자 음수처리
    minus = False
    if input_str[0] == '-':
        minus = True
        input_str = input_str[1:]
    nums = deque(map(int, re.split("\+|-|\*|/", input_str)))
    if minus:
        nums[0] *= -1

    # 연산자 파싱
    ops = deque(re.split("[0-9]+", input_str)[1:-1])

    # 연산자가 두 개 이상인 동안 계산 진행
    while len(ops) > 1:
        # 연산자 우선순위가 같은 경우
        if priority[ops[0]] == priority[ops[-1]]:
            res1 = calc(nums[0], nums[1], ops[0])
            res2 = calc(nums[-2], nums[-1], ops[-1])

            # 계산 결과가 큰 쪽을 우선시
            # 결과값이 같을경우 앞쪽을 우선시
            if res1 >= res2:
                nums.popleft()
                nums[0] = res1
                ops.popleft()
            else:
                nums.pop()
                nums[-1] = res2
                ops.pop()

        # 앞쪽 우선순위가 높은 경우
        elif priority[ops[0]] > priority[ops[-1]]:
            res = calc(nums[0], nums[1], ops[0])
            nums.popleft()
            nums[0] = res
            ops.popleft()

        # 뒤쪽 우선순위가 높은 경우
        else:
            res = calc(nums[-2], nums[-1], ops[-1])
            nums.pop()
            nums[-1] = res
            ops.pop()

    # 계산해야할 연산자가 남아있지 않다면 바로 숫자 반환
    if not ops:
        return nums[0]

    # 마지막 계산결과 반환
    return calc(nums[0], nums[1], ops[0])


# 계산 함수
def calc(o1, o2, op):
    if op == '+':
        return o1 + o2
    if op == '-':
        return o1 - o2
    if op == '*':
        return o1 * o2
    # C++의 정수나눗셈 규칙에 따라 나눗셈
    if op == '/':
        return abs(o1) // abs(o2) * (-1 if o1 * o2 < 0 else 1)
