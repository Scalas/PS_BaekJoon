import sys

input = sys.stdin.readline


# 10093 숫자
# 두 수 사이의 수들의 수와 수들을 오름차순으로 정렬한 리스트를 구하는 문제
def sol10093():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    mid = range(a+1, b)
    return '\n'.join([str(len(mid)), ' '.join(map(str, mid))])
