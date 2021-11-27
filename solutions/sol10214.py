import sys

input = sys.stdin.readline


# 10214 Baseball
# 각 테스트케이스에 주어진 두 팀의 점수를 합산하여 승패를 구하는 문제
def sol10214():
    answer = []
    for _ in range(int(input())):
        y, k = 0, 0
        for _ in range(9):
            u, v = map(int, input().split())
            y += u
            k += v
        answer.append('Yonsei' if y> k else 'Korea' if k < y else 'Draw')
    return '\n'.join(answer)
