import sys

input = sys.stdin.readline


# 14696 딱지놀이
# 라운드별로 주어진 A, B 두사람의 딱지의 상태에 따라 각 라운드의 승자를 구하는문제
def sol14696():
    answer = []
    for _ in range(int(input())):
        a, *acards = map(int, input().split())
        b, *bcards = map(int, input().split())
        ac, bc = [0] * 4, [0] * 4
        for card in acards:
            ac[4-card] += 1
        for card in bcards:
            bc[4-card] += 1
        if ac > bc:
            answer.append('A')
        elif ac < bc:
            answer.append('B')
        else:
            answer.append('D')
    return '\n'.join(answer)
