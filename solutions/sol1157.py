import sys
from collections import Counter

input = sys.stdin.readline


# 1157 단어공부
# 단어에 가장 많이쓰인 알파벳을 출력하는 문제
def sol1157():
    c = sorted(Counter(input().rstrip().upper()).items(), key=lambda x: -x[1])
    if len(c) > 1 and c[0][1] == c[1][1]:
        print('?')
    else:
        print(c[0][0])
