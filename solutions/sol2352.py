import sys
from bisect import bisect_left

input = sys.stdin.read


# 2352 반도체 설계
# 1번부터 n번 반도체까지 연결되어야할 반대편 반도체 번호가 주어졌을때
# 선이 교차되지 않도록 반도체를 연결하는 최대 연결수를 구하는 문제
# 전깃줄 교차문제와 마찬가지로 lis 알고리즘을 사용하여 해결 가능한 문제이다.
def sol2352():
    n, f, *seq = map(int, input().split())
    lis = [f]
    for num in seq:
        if num > lis[-1]:
            lis.append(num)
        else:
            lis[bisect_left(lis, num)] = num
    return len(lis)
