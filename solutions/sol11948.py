import sys

input = sys.stdin.read


# 11948 과목선택
# 여섯 과목의 점수중 1~4과목에서 점수가높은 3개, 5~6 과목에서 점수가 높은 1개를 골랐을 때
# 점수의 합을 구하는 문제
def sol11948():
    scores = list(map(int, input().split()))
    return sum(scores) - min(scores[:4]) - min(scores[4:])
