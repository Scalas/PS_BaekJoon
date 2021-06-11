import sys

input = sys.stdin.read


# 8958 OX 퀴즈
# OX 퀴즈의 채점결과를 입력받아 점수를 계산하는 문제
def sol8958():
    answer = []
    _, *cases = input().split()
    for case in cases:
        answer.append(str(sum(map(cal, case.split('X')))))
    print('\n'.join(answer))


def cal(s):
    n = len(s)
    return n * (n + 1) // 2
