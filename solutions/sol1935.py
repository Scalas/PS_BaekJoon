import sys

input = sys.stdin.readline


# 후위 표기식 2
# 후위 표기식과 각 피연산자의 값이 주어졌을 때
# 후위 표기식의 계산 결과를 구하는 문제
def sol1935():
    n = int(input())
    expr = input().rstrip()
    nums = [int(input()) for _ in range(n)]
    st = []
    op = {'+', '-', '*', '/'}
    for c in expr:
        if c in op:
            o2 = st.pop()
            o1 = st.pop()
            st.append(calc(o1, o2, c))
        else:
            st.append(nums[ord(c) - ord('A')])
    return f'%.2f' % st[0]


def calc(o1, o2, op):
    if op == '+':
        return o1 + o2
    elif op == '-':
        return o1 - o2
    elif op == '*':
        return o1 * o2
    else:
        return o1 / o2
