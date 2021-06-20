from sys import stdin


# 11650 좌표 정렬하기
# 좌표를 x 값으로 오름차순, x 값이 같으면 y 값으로 오름차순 정렬하는 문제
# 파이썬의 경우 튜플형태로 정렬할 경우 자동으로 기준에맞게 정렬된다
def sol11650():
    stdin.readline()
    dots = [tuple(map(int, i.split())) for i in stdin]
    dots.sort()
    answer = [f'{x} {y}' for x, y in dots]
    print('\n'.join(answer))
