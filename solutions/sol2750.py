import sys

input = sys.stdin.read


# 2750 수 정렬하기
# 입력받은 수를 정렬 후 개행으로 구분하여 출력하는 문제
def sol2750():
    n, *nums = map(int, input().split())
    nums.sort()
    print('\n'.join(map(str, nums)))
