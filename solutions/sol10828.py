from sys import stdin

input = stdin.readline


# 10828 스택
# 간단한 스택을 구현하는 문제
def sol10828():
    n = int(input())
    stack = []
    answer = []
    for _ in range(n):
        cmd = input().split()
        if len(cmd) > 1:
            stack.append(cmd[1])
        elif cmd[0][0] == 'p':
            answer.append(stack.pop() if stack else '-1')
        elif cmd[0][0] == 't':
            answer.append(stack[-1] if stack else '-1')
        elif cmd[0][0] == 's':
            answer.append(str(len(stack)))
        elif cmd[0][0] == 'e':
            answer.append('0' if stack else '1')
    print('\n'.join(answer))
