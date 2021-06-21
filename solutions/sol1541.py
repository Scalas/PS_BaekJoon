import sys

input = sys.stdin.readline


# 1541 잃어버린 괄호
# 숫자와 +와 -로 이루어진 수식에 괄호를 적절히 넣어 최솟값을 만드는 문제
# -를 구분자로 수식을 나누어 각각 계산한 뒤
# 첫 번째 수식에서 나머지 수식을 모두 빼면 해결할 수 있다
def sol1541():
    ex = [sum(map(int, e.split('+'))) for e in input().split('-')]
    print(ex[0] - sum(ex[1:]))
