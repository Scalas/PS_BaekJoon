import sys

input = sys.stdin.readline


# 2476 주사위 게임
# 주사위를 세번 던져 가장 많은 상금을 얻은 사람을 구하는 문제
def sol2476():
    res = []
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        if a == b == c:
            res.append(a * 1000 + 10000)
        elif a == b or a == c:
            res.append(a * 100 + 1000)
        elif b == c:
            res.append(b * 100 + 1000)
        else:
            res.append(100 * max(a, b, c))
    return max(res)
