import sys

input = sys.stdin.readline


# 2754 학점계산
# 학점이 주어지면 해당하는 평점을 출력하는 문제
def sol2754():
    score = {
        'A+':4.3, 'A0':4.0, 'A-':3.7,
        'B+':3.3, 'B0':3.0, 'B-':2.7,
        'C+':2.3, 'C0':2.0, 'C-':1.7,
        'D+':1.3, 'D0':1.0, 'D-':0.7,
        'F':0.0
    }
    return score[input().rstrip()]
