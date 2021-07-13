import sys

input = sys.stdin.readline


# 1004 어린 왕자
# 한점에서 다른점으로 이동할 때 원에 닿는 횟수의 최솟값을 구하는문제
# 한 점은 포함하지만 다른 한점은 포함하지 않는 원의 갯수를 구하면 풀 수 있다
def sol1004():
    answer = []
    for t in range(int(input())):
        sx, sy, ex, ey = map(int, input().split())
        res = 0
        for i in range(int(input())):
            x, y, r = map(int, input().split())
            if (((x - sx) ** 2 + (y - sy) ** 2) ** .5 < r) != (((x - ex) ** 2 + (y - ey) ** 2) ** .5 < r):
                res += 1
        answer.append(str(res))
    print('\n'.join(answer))
