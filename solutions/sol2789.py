import sys

input = sys.stdin.readline


# 2789 유학 금지
# 주어진 문자열에서 CAMBRIDGE 에 속하는 문자를 모두 제거한 문자열을 구하는 문제
def sol2789():
    banned = set('CAMBRIDGE')
    return ''.join([c for c in input().rstrip() if c not in banned])
