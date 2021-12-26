import sys

input = sys.stdin.read


# 15989 1, 2, 3 더하기 4
# 1, 2, 3 을 더하여 n을 만들 수 있는 경우의 수를 구하는 문제
# 단, 수의 조합은 같고 순서만이 다른경우는 하나의 경우로 간주한다.
def sol15989():
    _, *case = map(int, input().split())
    dp = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 1]]
    for i in range(4, max(case)+1):
        dp.append([dp[-1][0], sum(dp[-2][:2]), sum(dp[-3])])

    return '\n'.join(map(str, [sum(dp[c]) for c in case]))
