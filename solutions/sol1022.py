import sys

input = sys.stdin.readline


# 1022 소용돌이 예쁘게 출력하기
# 가운데 1부터 시작하여 소용돌이
# r1, c1 부터 r2, c2까지의
def sol1022():
    r1, c1, r2, c2 = map(int, input().split())

    def square(r, c):
        if r == c == 0:
            return 1
        layer = max(abs(r), abs(c))
        start = (layer * 2 - 1) ** 2 + 1
        end = (layer * 2 + 1) ** 2
        side = (end - start + 1) // 4
        if c == layer and r < layer:
            return start + (layer - r - 1)
        start += side
        if r == -layer and c < layer:
            return start + (layer - c - 1)
        start += side
        if c == -layer and r > -layer:
            return start + (r + layer - 1)
        start += side
        if r == layer and c > -layer:
            return start + (c + layer - 1)

    answer = []
    max_num = 0
    for i in range(r1, r2 + 1):
        line = [square(i, j) for j in range(c1, c2 + 1)]
        answer.append(line)
        max_num = max(max_num, max(line))
    max_digit = digit(max_num)

    for i in range(len(answer)):
        answer[i] = ' '.join(map(lambda x: ' ' * (max_digit - digit(x)) + str(x), answer[i]))

    return '\n'.join(answer)


def digit(num):
    res = 0
    while num:
        res += 1
        num //= 10
    return res
