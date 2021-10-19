import sys

input = sys.stdin.readline


# 10799 쇠막대기
# 인접한 괄호쌍이 쇠막대를 자르는 레이저, 그렇지 않은 괄호쌍은 쇠막대라고 할 때
# 만들어진 쇠막대의 갯수를 구하는 문제
def sol10799():
    par = input().rstrip()

    # 인접한 괄호를 모두 '|' 로 치환 - 레이저
    par = par.replace('()', '|')

    answer = 0
    bar = 0
    for p in par:
        # 열린 괄호마다 자를 쇠막대 갯수 증가
        if p == '(':
            bar += 1

        # 닫힌 괄호마다 자를 쇠막대 갯수 감소, 만들어진 쇠막대 갯수 하나 증가
        elif p == ')':
            bar -= 1
            answer += 1

        # 레이저마다 만들어진 쇠막대갯수 현재 자를 쇠막대 갯수만큼 증가
        else:
            answer += bar

    return answer
