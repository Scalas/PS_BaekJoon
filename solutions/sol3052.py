import sys

input = sys.stdin.read


# 입력받은 수들을 각각 42로 나눈 나머지를 구하고
# 그 중 서로 다른 나머지의 갯수를 출력하는 문제
# 각 숫자에 나머지 연산을 취한 뒤 그 결과를 집합으로 변환하면 중복값을 제거한 결과를 얻을 수 있다.
def sol3052():
    print(len(set(map(mod, map(int, input().split())))))


def mod(n):
    return n % 42
