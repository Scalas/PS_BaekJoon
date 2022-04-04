import sys
from bisect import bisect_left

input = sys.stdin.readlines


# 3745 오름세
# 각 테스트케이스에 주가의 갯수와 주가 리스트가 주어졌을 때
# 주가 리스트에서 최장 증가 수열을 찾는 문제
def sol3745():
    answer = []
    case = input()
    for i in range(0, len(case), 2):
        n = int(case[i])
        f, *stocks = list(map(int, case[i+1].split()))
        lis = [f]
        for stock in stocks:
            if stock > lis[-1]:
                lis.append(stock)
            else:
                lis[bisect_left(lis, stock)] = stock
        answer.append(len(lis))
    return '\n'.join(map(str, answer))
