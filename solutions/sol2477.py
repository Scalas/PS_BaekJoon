import sys

input = sys.stdin.readline


# 2477 참외밭
# 참외밭 1제곱미터당 참외의 갯수 k와 ㄱ자모양 참외밭의 변의 길이가 반시계방향으로 주어졌을 때
# 참외의 갯수를 구하는 문제
def sol2477():
    k = int(input())
    length = []
    dcount = [0] * 5
    for i in range(6):
        d, l = map(int, input().split())
        length.append((d, l))
        dcount[d] += 1

    while dcount[length[0][0]] == 1:
        length.append(length.pop(0))

    while dcount[length[-1][0]] == 2:
        length.insert(0, length.pop())

    return (length[-1][1] * length[-2][1] - length[1][1] * length[2][1]) * k
