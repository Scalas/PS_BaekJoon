import sys

input = sys.stdin.readline


# 1126 같은 탑
# n개의 블록의 높이가 주어졌을 때 그 블록들로 두 개의 탑을 쌓아
# 두 탑의 높이가 같도록 할 때 탑의 최대높이를 구하는 문제
# 단, 탑의 높이가 0인 경우는 -1을 출력
def sol1126():
    n = int(input())
    blocks = [0, *map(int, input().split())]
    total = sum(blocks)
    dp = [[-1] * (total+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(1, n+1):
        # i번째 블록의 높이
        block = blocks[i]

        for j in range(total+1):
            res = -1
            # 블록을 사용하지 않는 경우
            # 이전 단계에서도 같은 높이차였던 경우의 두 탑중 최대높이를 그대로 가져온다
            res = max(res, dp[i-1][j])

            # 블록을 어느 한쪽에 쌓아 j만큼의 높이차가 되도록 하는경우
            diff1, diff2, diff3 = j-block, block-j, block+j
            if diff1 >= 0 and dp[i-1][diff1] >= 0:
                res = max(res, dp[i-1][diff1] + block)
            if diff2 >= 0 and dp[i-1][diff2] >= 0:
                res = max(res, dp[i-1][diff2] + j)
            if diff3 <= total and dp[i-1][diff3] >= 0:
                res = max(res, dp[i-1][diff3])
            dp[i][j] = res

    return dp[-1][0] if dp[-1][0] else -1
