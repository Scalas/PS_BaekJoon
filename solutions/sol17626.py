import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline


# 17626 Four Squares
# 자연수 n을 최소한의 제곱수의 합으로 나타내기 위해 필요한 제곱수의 갯수를 구하는 문제

# bottom-up 동적계획법을 사용할경우 pypy를 사용하지 않으면 시간초과가 발생
def sol17626():
    n = int(input())
    dp = [0] * (n+1)
    dp[1] = 1
    sq_list = [i**2 for i in range(1, int(n**.5)+1)]
    for i in range(2, n+1):
        minv = 5
        for sq in sq_list:
            if sq > i:
                break
            minv = min(minv, dp[i-sq]+1)
        dp[i] = minv
    return dp[n]


# 조합을 사용하여 미리 가능한 경우의수를 구해놓고 포함여부만으로 구할 경우 python3 로도 통과
def sol17626_2():
    n = int(input())
    sq_list = set([i**2 for i in range(1, int(n**.5)+1)])
    sq_list_second = set(map(sum, combinations_with_replacement(sq_list, 2)))
    sq_list_third = set(map(sum, combinations_with_replacement(sq_list, 3)))
    return 1 if n in sq_list else 2 if n in sq_list_second else 3 if n in sq_list_third else 4
