import sys

input = sys.stdin.readline


# 11062 카드 게임
# 근우와 명우가 n개의 카드에서 서로 번갈아가며 맨앞 또는 맨뒤의 카드를 가져가는 게임을 한다.
# 근우부터 게임을 시작하고 서로가 최대한 가져간 카드에 쓰여진 수의 합이 크도록 하기위해
# 최선의 선택을 한다고 할때, 근우가 얻을 수 있는 카드에 쓰여진 수의 합의 최댓값을 구하는 문제
def sol11062():
    answer = []
    for _ in range(int(input())):
        n = int(input())
        cards = list(map(int, input().split()))

        # 현재 카드뭉치의 시작점이 i일 때
        # 현재가 근우의 턴이라면 근우가 얻을 수 있는 점수의 최댓값은 dp[i][0]
        # 현재가 명우의 턴이라면 근우가 얻을 수 있는 점수의 최댓값은 dp[i][1]
        dp = [(cards[i], 0) for i in range(n)]

        # 카드뭉치의 맨 왼쪽과 맨 오른쪽의 인덱스 차이(카드뭉치의 길이-1)
        for diag in range(1, n):
            ndp = []
            # 카드뭉치의 시작 인덱스
            for i in range(n-diag):
                # 카드뭉치의 끝 인덱스
                j = i + diag

                # 근우가 맨 앞 카드(cards[i])를 가져갈 경우와 맨 뒤 카드(cards[j])를 가져갈 경우중 최댓값
                maxv = max(cards[i] + dp[i+1][1], cards[j] + dp[i][1])

                # 명우가 맨 앞 카드를 가져갈 경우와 맨 뒤 카드를 가져갈 경우중 최솟값
                minv = min(dp[i+1][0], dp[i][0])
                ndp.append((maxv, minv))
            dp = ndp
        answer.append(dp[0][0])
    return '\n'.join(map(str, answer))
