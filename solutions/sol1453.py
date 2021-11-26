import sys

input = sys.stdin.read


# 1453 피시방 알바
# 이미 사용중인 자리를 고른 손님의 수를 구하는 문제
# 수열 전체 길이 - 중복을 제거한 수열의 길이
def sol1453():
    n, *customers = map(int, input().split())
    return len(customers) - len(set(customers))
