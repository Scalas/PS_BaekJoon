import sys

input = sys.stdin.readline


# 17389 보너스 점수
# 연속정답에 보너스가 붙는 채점방식으로 점수를 구하는 문제
def sol17389():
    n = int(input())
    sheet = input().rstrip()
    score = 0
    for i in range(n):
        score += (sheet[i] == 'O') * (i + 1)
    score += sum(map(lambda x: x * (x - 1) // 2, [len(x) for x in sheet.split('X')]))
    return score

