import sys

input = sys.stdin.read


# 10807 개수 세기
# 배열 내의 특정 숫자의 갯수를 구하는 문제
def sol10807():
    n, *seq = map(int, input().split())
    return seq[:-1].count(seq[-1])
