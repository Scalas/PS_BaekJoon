import sys

input = sys.stdin.readline


# 8895 막대 배치
# 막대의 갯수 n과 막대의 나열을 왼쪽에서 봤을 때 보이는 막대의 갯수 l, 오른쪽에서 봤을 때 보이는 막대의 갯수 r이 주어질 때
# 주어진 값이 나올 수 있는 막대의 배치의 수를 구하는 문제
def sol8895():
    # dp[i][l][r]은 블록이 i개일 때 왼쪽에서 l개, 오른쪽에서 r개 보일 때의 경우의 수
    dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

    # 처음에는 블록이 한개이므로 왼쪽 1, 오른쪽 1의 한가지 경우 뿐
    dp[1][1][1] = 1

    # 블록을 추가해나가며 경우의 수를 갱신
    for i in range(2, 21):
        for j in range(1, i + 1):
            for k in range(1, i + 1):
                dp[i][j][k] = dp[i-1][j-1][k] + dp[i-1][j][k-1] + dp[i-1][j][k] * (i - 2)

    # 모든 쿼리에 대해 배치의 수를 구함
    answer = []
    for _ in range(int(input())):
        u, v, w = map(int, input().split())
        answer.append(dp[u][v][w])

    return '\n'.join(map(str, answer))
