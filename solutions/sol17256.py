import sys

input = sys.stdin.read


# 17256 달달함이 넘쳐흘러
# 세 개의 자연수로 이루어진 두 케이크수간의 연산 결과와 피연산자 하나가 주어졌을 때
# 나머지 하나의 피연산자를 구하는 문제
def sol17256():
    u, v, w, x, y, z = map(int, input().split())
    return ' '.join(map(str, [x - w, y // v, z - u]))
