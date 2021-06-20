from sys import stdin


# 11651 좌표 정렬하기 2
# 좌표를 y 값으로 오름차순, y 값이 같으면 x 값으로 오름차순 정렬하는 문제
# 11650 문제의 풀이에서 sort 함수에 key 값으로 y 값을 x 값보다 우선하여 정렬하도록 람다함수를 전달
def sol11651():
    stdin.readline()
    dots = [tuple(map(int, i.split())) for i in stdin]
    dots.sort(key=lambda x:(x[1], x[0]))
    answer = [f'{x} {y}' for x, y in dots]
    print('\n'.join(answer))
