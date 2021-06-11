import sys

input = sys.stdin.read


# 4344 평균은 넘겠지
# 각 케이스의 학생들의 점수를 입력받아 평균을 넘는 학생의 비율을
# 반올림하여 소숫점 세번째 자리까지의 퍼센티지로 출력하는 문제
def sol4344():
    answer = []
    _, *cases = input().splitlines()
    for case in cases:
        n, *scores = map(int, case.split())
        avg = sum(scores) / n
        answer.append('%.03f%%' % (len([i for i in scores if i > avg]) * 100 / n))
    print('\n'.join(answer))
