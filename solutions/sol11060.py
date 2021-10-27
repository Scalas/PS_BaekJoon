import sys

input = sys.stdin.readline
INF = 1000


# 11060 점프 점프
# 칸마다 점프가능한 최대칸수가 적힌 직선형 보드의 맨 왼쪽에서 맨 오른쪽으로 가기 위한
# 최소 이동횟수를 구하는 문제 간단한 동적계획법으로 해결 가능
def sol11060():
    n = int(input())
    board = list(map(int, input().split()))
    jump = [INF] * n
    jump[0] = 0
    for i in range(n):
        for j in range(i+1, min(i+1+board[i], n)):
            jump[j] = min(jump[j], jump[i]+1)
    return jump[-1] if jump[-1] != INF else -1
