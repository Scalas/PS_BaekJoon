import sys

input = sys.stdin.readline


# 9295 주사위
# 각 테스트케이스로 주어진 두 수의 합을 구하는 문제
def sol9295():
    return '\n'.join(['Case %d: %d' % (i, sum(map(int, input().split()))) for i in range(1, int(input())+1)])
