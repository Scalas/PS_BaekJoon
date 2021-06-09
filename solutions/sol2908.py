import sys

input = sys.stdin.readline


# 2908 상수
# 입력된 두개의 세자리 수를 뒤집은 후 그중 더 큰 수를 출력하는 문제
def sol2908():
    a, b = input().split()
    print(max(int(a[::-1]), int(b[::-1])))
