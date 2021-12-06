import sys

input = sys.stdin.readline


# 2857 FBI
# 이름에 FBI가 들어가는 요원이 몇번째 입력인지 구하는 문제
def sol2857():
    answer = []
    for i in range(5):
        if 'FBI' in input().rstrip():
            answer.append(i+1)

    return ' '.join(map(str, answer)) if answer else 'HE GOT AWAY!'
