import sys

input = sys.stdin.readline


# 1065 한수
# 각 자릿수가 등차를 이루는 양의정수 x를 구하는 문제
def sol1065():
    answer = 0
    for i in range(1, int(input()) + 1):
        if check(i):
            answer += 1
    print(answer)


def check(n):
    num = list(map(int, list(str(n))))
    d = [num[i + 1] - num[i] for i in range(len(num) - 1)]
    for i in range(1, len(d)):
        if d[i] != d[0]:
            return False
    return True
