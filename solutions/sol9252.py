import sys


# 9252 LCS 2
# 최장 공통수열의 길이와 최장공통수열을 구하는 문제

# 첫 번째 시도
# O(NM)의 동적계획법을 사용한 풀이
# s1[i] == s2[j] 일 경우 s1[i-1] 와 s2[j-1]를 비교했을 때 까지보다 공통부분이 1만큼 길어진다.
# 그렇지 않을 경우 s1[i-1], s2[j]를 비교했을 때와 s1[i], s2[j-1]를 비교했을 떄의 공통부분중 더 긴쪽과 같다
# 경로를 추적하기위해 매번 이전단계의 인덱스쌍을 저장한다.
def sol9252(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    trace = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                trace[i+1][j+1] = (i, j)
            else:
                if dp[i][j+1] < dp[i+1][j]:
                    dp[i+1][j+1] = dp[i+1][j]
                    trace[i+1][j+1] = trace[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
                    trace[i+1][j+1] = trace[i][j+1]
    l = str(dp[-1][-1])
    lcs = []
    t = trace[-1][-1]
    if s1[-1] == s2[-1]:
        lcs.append(s1[-1])
        t = trace[t[0]][t[1]]
    while t:
        i, j = t
        lcs.append(s1[i])
        t = trace[i][j]
    lcs = ''.join(lcs[::-1])
    return '\n'.join((l, lcs))
