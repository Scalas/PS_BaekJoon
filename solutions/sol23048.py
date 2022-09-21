import sys

input = sys.stdin.readline


# 23048 자연수 색칠하기
# n 개의 자연수를 최소한의 색으로 색칠하는 방법을 찾는 문제.
# 단, 서로소인 두 수는 서로 다른 색으로 칠해져야한다.
def sol23048():
    n = int(input())

    # 에라토스테네스의 체를 응용하여 해결 가능
    colored = [0] * n
    colored[0] = 1
    color = 2
    for i in range(2, n + 1):
        if colored[i - 1]:
            continue

        colored[i - 1:n:i] = [color] * (n // i)
        color += 1

    return '\n'.join([str(color - 1), ' '.join(map(str, colored))])
