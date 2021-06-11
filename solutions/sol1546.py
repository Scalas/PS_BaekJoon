import sys

input = sys.stdin.read


# 1546 평균
# 입력받은 점수를 조작한 뒤의 평균값을 구하는 문제
def sol1546():
    _, *scores = map(int, input().split())
    print(sum(scores) / max(scores) / len(scores) * 100)

