import sys

input = sys.stdin.readline


# 16139 인간-컴퓨터 상호작용
# 문자열 s 에서 좌우 인덱스 사이에 문자 c가 몇개 들어가는지 구하는 문제
def sol16139():
    s = input().rstrip()
    count = [[0] * 26 for _ in range(len(s) + 1)]

    for i in range(len(s)):
        idx = ord(s[i]) - 97
        count[i] = count[i - 1][:]
        count[i][idx] += 1

    answers = []
    for _ in range(int(input())):
        c, left, right = map(mapper, input().split())
        answers.append(count[right][c] - count[left - 1][c])

    return '\n'.join(map(str, answers))


def mapper(inp):
    if inp.isdigit():
        return int(inp)
    else:
        return ord(inp) - 97
