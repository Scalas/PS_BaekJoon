import sys

input = sys.stdin.readline


# 9610 사분면
# 주어진 좌표들중 각 사분면과 좌표축에 속한 것이 몇개씩인지 구하는 문제
def sol9610():
    answer = [0, 0, 0, 0, 0]
    for _ in range(int(input())):
        x, y = map(int, input().split())
        m = x * y
        if not m:
            answer[4] += 1
        elif m > 0:
            if x > 0:
                answer[0] += 1
            else:
                answer[2] += 1
        else:
            if x > 0:
                answer[3] += 1
            else:
                answer[1] += 1
    return 'Q1: %d\nQ2: %d\nQ3: %d\nQ4: %d\nAXIS: %d' % tuple(answer)
