import sys

input = sys.stdin.readline


# 9076 점수 집계
# 다섯개의 점수중 최대, 최소 점수를 제외한 점수의 합을 구하는문제
# 만약 최대, 최소점수를 제외한 뒤 남은 점수중 최대, 최소 점수의 차가 4 이상이라면 KIN을 출력한다
def sol9076():
    answer = []
    for _ in range(int(input())):
        score = sorted(list(map(int, input().split())))[1:-1]
        if score[-1] - score[0] >= 4:
            answer.append('KIN')
        else:
            answer.append(str(sum(score)))

    return '\n'.join(answer)