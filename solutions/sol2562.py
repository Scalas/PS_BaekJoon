import sys

input = sys.stdin.read


# 2562 최댓값
# 리스트의 최댓값과 그 인덱스를 구하는 문제
def sol2562():
    num = list(map(int, input().split()))
    m = mi = 0
    for i in range(9):
        if (num[i] > m):
            m = num[i]
            mi = i
    print(m, mi + 1, sep='\n')
