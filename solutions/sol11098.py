import sys

input = sys.stdin.readline


# 11098 첼시를 도와줘!
# 몸값이 가장 비싼 선수의 이름을 구하는 문제
def sol11098():
    answer = []
    for _ in range(int(input())):
        answer.append(max([[*map(lambda x: int(x) if x.isdigit() else x, input().split())] for _ in range(int(input()))])[1])
    return '\n'.join(answer)
