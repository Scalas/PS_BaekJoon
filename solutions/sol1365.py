import sys
from bisect import bisect_left

input = sys.stdin.readline


# 1365 꼬인 전깃줄
# 1~n번 전봇대에 연결된 반대쪽 전봇대의 번호가 주어졌을때
# 교차하는 전깃줄을 없애기 위해 끊어야할 전선의 갯수를 구하는 문제
# 전형적인 lis 알고리즘을 활용하는 문제
def sol1365():
    n = int(input())
    f, *seq = list(map(int, input().split()))
    lis = [f]
    for num in seq:
        if num > lis[-1]:
            lis.append(num)
        else:
            lis[bisect_left(lis, num)] = num
    return n - len(lis)
