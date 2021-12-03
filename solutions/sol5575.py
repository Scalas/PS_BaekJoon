import sys

input = sys.stdin.readline


# 5575 타임 카드
# 세 사람의 출근 시간과 퇴근시간이 주어졌을때 근무 시간을 시 분 초로 나누어 구하는 문제
def sol5575():
    answer = []
    for _ in range(3):
        h, m, s, eh, em, es = map(int, input().split())
        time = eh * 3600 + em * 60 + es - h * 3600 - m * 60 - s
        h = time // 3600
        time %= 3600
        m = time // 60
        s = time % 60
        answer.append(' '.join(map(str, [h, m, s])))
    return '\n'.join(answer)
