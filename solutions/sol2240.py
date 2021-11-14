import sys

input = sys.stdin.readline


# 2240 자두나무
# 1번 나무와 2번 나무 사이를 최대 w번 이동할 수 있고
# t초 동안 1초에 한번 1번 혹은 2번 나무에서 자두가 떨어질 때
# 잡을 수 있는 자두의 최대 갯수를 구하는 문제
def sol2240():
    t, w = map(int, input().split())
    fall = list(map(int, sys.stdin.read().split()))

    # dp[i][j] 는 i초에 j번 이동한 상태일 때 잡을 수 있는 자두의 최대 갯수
    dp = [[0] * (w+1) for _ in range(t+1)]

    # 처음엔 1번나무에 있기 때문에 첫 번째 자두가 1이라면 dp[1][0] = 1
    # 2라면 dp[1][1] = 1
    if fall[0] == 1:
        dp[1][0] = 1
    else:
        dp[1][1] = 1

    # dp[i][0] 은 1번자두가 떨어지면 dp[i-1][0] + 1, 2번자두가 떨어지면 dp[i-1][0]
    # dp[i][j] 는 현재 위치의 자두가 떨어지면 한번 이동하여 자두를 잡은경우(dp[i-1][j-1])와
    # 그자리에서 자두를 잡은경우(dp[i-1][j]) 중 최댓값에 1을 더한 값이 된다.
    # 현재 위치와 다른 위치에서 자두가 떨어지면 이동없이 자두를 버린 경우(dp[i-1][j])의 값이 된다.
    for i in range(2, t+1):
        dp[i][0] = dp[i-1][0] + (1 if fall[i-1] == 1 else 0)
        for j in range(1, min(w+1, i+1)):
            if j % 2:
                if fall[i-1] == 1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            else:
                if fall[i-1] == 2:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1

    # t초 째에 잡을 수 있는 자두의 갯수 중 최댓값을 반환
    return max(dp[t])
