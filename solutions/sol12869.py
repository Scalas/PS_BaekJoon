import sys
from math import ceil

input = sys.stdin.readline
double_case = [(9, 3, 0), (3, 9, 0)]
triple_case = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]
INF = 61


# 12869 뮤탈리스크
def sol12869():
    n = int(input())
    scv = list(map(int, input().split()))
    while len(scv) < 3:
        scv.append(0)
    scv.sort(reverse=True)

    # dp[i][j][k] 는 scv의 체력이 내림차순으로 i, j, k 일 때
    # 모두 파괴하기 위해 필요한 최소 공격 횟수
    dp = [[[0] * 61 for _ in range(61)] for _ in range(61)]

    def dfs(s1, s2, s3, cnt):
        if not dp[s1][s2][s3]:
            # 1대 남은경우
            if cnt == 1:
                # 남은 scv 의 체력을 9로 나눈 값을 올림한 값
                dp[s1][s2][s3] = ceil(s1 / 9)

            # 2대 남은 경우
            elif cnt == 2:
                res = INF
                for case in double_case:
                    ns1, ns2, ns3, nc = after_attack(s1, s2, s3, case)
                    res = min(res, 1 + (dfs(ns1, ns2, ns3, cnt) if nc else 0))
                dp[s1][s2][s3] = res
            # 3대 남은 경우
            else:
                res = INF
                for case in triple_case:
                    ns1, ns2, ns3, nc = after_attack(s1, s2, s3, case)
                    res = min(res, 1 + (dfs(ns1, ns2, ns3, cnt) if nc else 0))
                dp[s1][s2][s3] = res
        return dp[s1][s2][s3]

    return dfs(*scv, n)


# scv 의 남은 체력이 s1, s2, s3 이고 뮤탈리스크의 공격이 case 와 같이 들어올 때
# 공격 후 scv의 체력을 내림차순으로 정렬한 값과 남아있는 scv의 수를 반환
def after_attack(s1, s2, s3, case):
    res = list()
    res.append(max(s1-case[0], 0))
    res.append(max(s2-case[1], 0))
    res.append(max(s3-case[2], 0))
    res.sort(reverse=True)
    res.append(3-res.count(0))
    return res
