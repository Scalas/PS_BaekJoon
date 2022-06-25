import sys

input = sys.stdin.readline


# 17425 약수의 합
# n까지의 자연수의 약수의 합을 모두 더한 값을 구하는 문제
def sol17425():
    answers = []
    g = [1] * 1000001
    for i in range(2, 1000001):
        for j in range(i, 1000001, i):
            g[j] += i
    for i in range(1, 1000000):
        g[i + 1] += g[i]

    for _ in range(int(input())):
        answers.append(g[int(input())])

    return '\n'.join(map(str, answers))
