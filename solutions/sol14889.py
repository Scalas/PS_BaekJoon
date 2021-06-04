import sys

input = sys.stdin.readline


# 14889 스타트와 링크
# 1부터 n 까지의 선수를 두 팀으로 나누어 각 팀의 시너지 수치의 차의 최솟값을 구하는 문제

# 1차 시도 - 실제로 두 팀을 나누어 각각의 시너지 수치를 계산한 뒤 그 차의 최솟값을 구함
# 풀리긴 하지만 파이썬 기준 너무 많은 시간이 소비됨
def sol14889():
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    print(dfs(n, table, [], [], 0))


def dfs(n, table, team_start, team_link, player):
    if (player == n):
        return abs(power(team_start, table) - power(team_link, table))
    tm = n // 2
    res = float('inf')
    if (len(team_start) < tm):
        team_start.append(player)
        res = min(res, dfs(n, table, team_start, team_link, player + 1))
        team_start.pop()

    if (len(team_link) < tm):
        team_link.append(player)
        res = min(res, dfs(n, table, team_start, team_link, player + 1))
        team_link.pop()

    return res


def power(team, table):
    res = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            res += (table[team[i]][team[j]] + table[team[j]][team[i]])
    return res


# 다른 풀이를 보고 2차시도
# 각 선수 한명으로 인해 생기는 시너지 효과를 모두 더한 값의 집합 parts
# parts 의 값을 모두 더하면 table 의 모든 값을 두번 더한게 되며 이를 2로 나누면 table 의 모든 값의 합(total)이 된다
# 한 팀의 멤버만 구성해도 다른 팀의 멤버는 남은 모든 선수가 되며
# 그 멤버들의 각 parts 값을 모두 더해서 total 에서 빼면
# 결과적으로 두 팀의 시너지 수치의 차와 같은 값이 된다 (그림을 그려서 확인함)
# 팀을 짜는데 걸리는 시간도 대폭 줄었으며 점수의 계산도 빨라져 1차 시도보다 훨씬 빠른속도로 해결됨
# 완전탐색으로 찾아낸 팀의 조합을 combinations 를 사용하여 구하는 법도 있지만 결국 방법은 같기때문에 따로 작성하지 않음
def sol14889_2():
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    parts = [sum([table[x][i] + table[i][x] for x in range(n)]) for i in range(n)]
    total = sum(parts) // 2
    print(dfs_2(n, total, parts, [], 0))


def dfs_2(n, total, parts, team, player):
    if len(team) == n // 2:
        return power_2(team, total, parts)

    res = float('inf')
    if len(team) + n - player < n // 2:
        return res
    team.append(player)
    res = min(res, dfs_2(n, total, parts, team, player + 1))
    team.pop()
    res = min(res, dfs_2(n, total, parts, team, player + 1))
    return res


def power_2(team, total, parts):
    res = total
    res -= sum([parts[p] for p in team])
    return abs(res)

