import sys

input = sys.stdin.readline


# 10103 주사위 게임
# 100점에서 시작하여 주사위를 던져 작은 눈이 나온쪽이 큰쪽 눈만큼 점수를 잃을 때
# 게임이 끝난 후 두 플레이어의 점수를 구하는 문제
def sol10103():
    answer = [100, 100]
    for _ in range(int(input())):
        u, v = map(int, input().split())
        if u < v:
            answer[0] -= v
        elif u > v:
            answer[1] -= u
    return '\n'.join(map(str, answer))
