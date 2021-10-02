import sys

input = sys.stdin.readline


# 2096 내려가기
# n x 3 배열의 0번재 행부터 한 행마다 하나의 값씩을 선택하고
# 다음 열에서는 선택한 값의 아래에 있는 값 또는 그 값과 인접한 값만을 선택가능할 때
# 마지막 행 까지 값을 선택하여 얻을 수 있는 숫자의 합의 최댓값, 최솟값을 구하는 문제
def sol2096():
    n = int(input())

    # 최댓값
    maxs = [0, 0, 0]

    # 최솟값
    mins = [0, 0, 0]

    # n 개의 열에서 숫자를 선택
    for _ in range(n):
        # 0, 1, 2 번째 열의 값
        a, b, c = map(int, input().split())

        # 0, 1, 2 번째 값을 고르기 위해 이전 값으로 가능한 리스트는 각각 0, 1번째, 0, 1, 2 번째, 1, 2 번째 수
        maxs = max(maxs[:2]) + a, max(maxs) + b, max(maxs[1:]) + c
        mins = min(mins[:2]) + a, min(mins) + b, min(mins[1:]) + c

    # 출력 형식에 맞춰 최댓값, 최솟값 반환
    return ' '.join(map(str, [max(maxs), min(mins)]))
