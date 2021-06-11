import sys

input = sys.stdin.read


# 2577 숫자의 개수
# 세 자연수 A, B, C의 곱에 사용된 0부터 9까지의 수의 갯수를 각각 구하는 문제
def sol2577():
    a, b, c = map(int, input().split())
    answer = [0] * 10
    for c in map(int, str(a * b * c)):
        answer[c] += 1
    print('\n'.join(map(str, answer)))

