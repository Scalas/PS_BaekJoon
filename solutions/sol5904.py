import sys
from bisect import bisect_left


# 5904 Moo 게임
# 0번째 Moo 문자열이 'm o o' 이고
# k번째 Moo 문자열은 <k-1번째 Moo문자열><m o ... o(o는 k + 2개)><k-1번째 Moo문자열> 이다
# 이 때, Moo 문자열의 n번째 문자를 구하는 문제
def sol5904():
    n = int(input())
    if n == 1:
        return 'm'
    if n <= 3:
        return 'o'

    dp = [3]
    while n > dp[-1]:
        dp.append(dp[-1] * 2 + len(dp) + 3)
    dp.append(0)

    def search(idx, layer):
        if idx <= dp[layer - 1]:
            return search(idx, layer - 1)
        if idx == dp[layer - 1] + 1:
            return 'm'
        if idx <= dp[layer - 1] + (layer + 3):
            return 'o'
        else:
            return search(idx - (dp[layer - 1] + layer + 3), layer - 1)

    return search(n, len(dp) -1)
