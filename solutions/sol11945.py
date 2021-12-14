import sys

input = sys.stdin.readline


# 11945 뜨거운 붕어빵
# 주어진 n * m 배열을 좌우로 뒤집어 출력하는 문제
def sol11945():
    n, m = map(int, input().split())
    return '\n'.join([input().rstrip()[::-1] for _ in range(n)])