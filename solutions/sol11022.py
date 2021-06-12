import sys

input = sys.stdin.readline


# 11022 A+B - 8
def sol11022():
    cn = 1
    answer = []
    for a, b in [map(int, i.split()) for i in sys.stdin.read().splitlines()[1:]]:
        answer.append(f'Case #{cn}: {a} + {b} = {a+b}')
        cn += 1
    print('\n'.join(answer))
