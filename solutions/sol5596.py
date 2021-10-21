import sys

input = sys.stdin.readline


# 5596 시험 점수
# 두 줄에 걸쳐 출력된 두 사람의 시험점수의 총합을 구한 뒤 그 중 큰 쪽을 구하는 문제
def sol5596():
    return max([sum(map(int, input().split())) for _ in range(2)])
