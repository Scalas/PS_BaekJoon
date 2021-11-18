import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


# 10835 카드 게임
# 각각 n개의 카드로 이뤄진 왼쪽, 오른쪽의 카드 뭉치가 있을 때
# 항상 왼쪽 맨 위의 카드를 버리거나 양쪽 맨위의 카드를 버릴 수 있고
# 오른쪽 맨 위의 카드가 왼쪽 맨 위의 카드보다 작다면 오른쪽 카드를 버릴 수 있으며
# 이 경우 오른쪽 맨 위 카드에 쓰여진 수만큼 점수를 얻는다
# 두 카드뭉치중 하나라도 0개가 되면 게임이 종료된다
# 이 때 게임이 종료될 때 까지 얻을 수 있는 최고점수를 구하는 문제
def sol10835():
    n = int(input())
    lcard = list(map(int, input().split()))
    rcard = list(map(int, input().split()))

    # dp[i][j] 는 왼쪽 카드를 i개, 오른쪽 카드를 j개 버린상태에서
    # 추가로 얻을 수 있는 최대점수
    dp = [[-1] * (n+1) for _ in range(n+1)]

    # 이미 한쪽 카드뭉치를 전부 버렸다면 더이상 점수를 얻을 수 없음
    for i in range(n+1):
        dp[i][n] = dp[n][i] = 0

    def dfs(lc, rc):
        if dp[lc][rc] < 0:
            # 오른쪽 카드를 버릴 수 있다면 오른쪽 카드를 버리고 점수를 얻는다
            if lcard[lc] > rcard[rc]:
                dp[lc][rc] = dfs(lc, rc+1) + rcard[rc]
            # 그렇지 않다면 왼쪽 또는 양쪽의 카드를 버린다
            else:
                dp[lc][rc] = max(dfs(lc+1, rc), dfs(lc+1, rc+1))

        return dp[lc][rc]

    # 카드를 하나도 버리지 않은 초기상태에서 얻을 수 있는 최대점수를 구한다
    return dfs(0, 0)

