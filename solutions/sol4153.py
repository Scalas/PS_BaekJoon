import sys

input = sys.stdin.read


# 4153 직각삼각형
# 주어진 삼각형의 세 변의 길이로 그 삼각형이 직각삼각형인지 판별하는 문제
def sol4153():
    answer = []
    for i in input().splitlines():
        sides = list(map(int, i.split()))
        if sides == [0, 0, 0]:
            break
        h = max(sides)
        sides.remove(h)
        a1, a2 = sides
        answer.append('right' if a1 ** 2 + a2 ** 2 == h ** 2 else 'wrong')
    print('\n'.join(answer))
