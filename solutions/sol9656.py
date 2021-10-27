import sys

input = sys.stdin.readline


# 9656 돌 게임
# 상근, 창영 둘이 번갈아가며 1개 또는 3개씩 집어서 마지막에 돌을 가져가는 사람이 지는 게임
# n개의 돌로 시작했을 때 이기는 사람을 구하는 문제
def sol9656():
    # 서로 실수를 하지 않는다면 돌이 짝수개일때는 상근이가, 홀수개일때는 창영이가 이기게 되어있다.
    return 'CY' if int(input()) % 2 else 'SK'
