import sys
from bisect import bisect_left

input = sys.stdin.readline


# 1965 상자넣기
# 앞에있는 상자를 뒤에있는 더 큰 상자에 넣을 수 있을 때
# 하나의 상자에 넣을 수 있는 상자의 갯수의 최댓값을 구해야한다
# 최장 증가 부분 수열의 길이를 구하는 문제와 동일
def sol1965():
    # 상자의 갯수
    n = int(input())

    # lis 알고리즘을 사용하여 최장 증가 부분 수열의 길이를 구하여 반환
    lis = [0]
    for s in map(int, input().split()):
        if s > lis[-1]:
            lis.append(s)
        else:
            lis[bisect_left(lis, s)] = s

    return len(lis) - 1
